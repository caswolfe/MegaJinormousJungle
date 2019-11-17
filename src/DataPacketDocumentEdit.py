import difflib
import hashlib
from enum import Enum
import logging
import json

try:
    from src.DataPacket import DataPacket
except ImportError as ie:
    try:
        # TODO: linux imports
        from DataPacket import DataPacket
    except ImportError as ie2:
        print('cant import???')
        exit(-1)


class DataPacketDocumentEdit(DataPacket):

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

        # default values
        self.old_text_hash: str = None
        self.action: Action = Action.UNDEFINED
        self.position: int = -1
        self.character: str = ''
        self.update_data_dict()

    def define_manually(self, old_text_hash, action, position: int, character: str) -> None:
        """
        Sets the parameters of the packet manually

        :param old_text_hash: The hash of the old text
        :param action: The action to be applied
        :param position: The position where the action will be applied
        :param character: The character which will be applied
        """
        self.old_text_hash = old_text_hash
        self.action = action
        self.position = position
        self.character = character
        self.update_data_dict()

    def update_data_dict(self) -> None:
        super().update_data_dict()
        self.data_dict.update({'old_text_hash': self.old_text_hash})
        self.data_dict.update({'action': self.action.value})
        self.data_dict.update({'position': self.position})
        self.data_dict.update({'character': self.character})

    def check_hash(self, text: str) -> bool:
        """
        Checks the hash of the provided text against the old_text_hash of the packet

        :param text: text to check

        :return: True if the hash's match
        """
        return self.get_text_hash(text) == self.old_text_hash

    @staticmethod
    def generate_first_change_packet(old_text: str, new_text: str):
        """
        Generates a DataPacketDocumentEdit off of the first difference between the two text's

        :param old_text: the old text
        :param new_text: the new text (with changes)

        :return: a single DataPacketDocumentEdit with the first detected change
        """

        old_text_hash = hashlib.sha1(old_text.encode()).hexdigest()
        to_ret_packet: DataPacketDocumentEdit = DataPacketDocumentEdit()
        for i, s in enumerate(difflib.ndiff(old_text, new_text)):
            if s[0] == ' ':
                pass
            elif s[0] == '-':
                action = Action.REMOVE
                position = i
                character = s[-1]
                to_ret_packet.define_manually(old_text_hash, action, position, character)
                return to_ret_packet
            elif s[0] == '+':
                action = Action.ADD
                position = i
                character = s[-1]
                to_ret_packet.define_manually(old_text_hash, action, position, character)
                return to_ret_packet
        return None

    @staticmethod
    def generate_packets_from_changes(old_text: str, new_text: str):
        """
        generates a list of DataPacketDocumentEdit's which will allow one to alter the old_text into the new_text

        :param old_text: the old text
        :param new_text: the new text (with changes)

        :return: a list of DataPacketDocumentEdit's which can be applied to the old_text (sequentially) to bring it up to new_text
        """

        generated_packets = list()
        current_text: str = old_text
        change = DataPacketDocumentEdit.generate_first_change_packet(current_text, new_text)
        while change is not None:

            generated_packets.append(change)
            if change.check_hash(current_text):
                current_text = DataPacketDocumentEdit.apply_packet(current_text, change)
            else:
                raise Exception("Hash Mismatch")

            change = DataPacketDocumentEdit.generate_first_change_packet(current_text, new_text)

        return generated_packets

    @staticmethod
    def apply_packet(text: str, packet):
        """
        Applies the provided packet to the provided string, raises an exception if text hash's mismatch

        :param text: text to apply the packet to
        :param packet: the packet to apply to the text

        :return: a new string with the new text
        """
        if packet.check_hash(text):
            return text[:packet.position] + packet.character + text[packet.position:]
        else:
            raise Exception("Hash Mismatch")

    @staticmethod
    def apply_multiple_packets(text: str, packets) -> str:
        """
        Applies multiple packets to the text

        :param text: text to apply the packets to
        :param packets: a list of packet to apply to the text sequentially

        :return: a new string with the new text
        """
        current_text = text
        for packet in packets:
            if packet.check_hash(current_text):
                current_text = DataPacketDocumentEdit.apply_packet(current_text, packet)
            else:
                raise Exception("Hash Mismatch")
        return current_text

    @staticmethod
    def get_text_hash(text: str) -> str:
        """
        returns the hash of the provided string

        :param text: string to get the hash of

        :return: the hash of the string
        """
        return hashlib.sha1(text.encode()).hexdigest()

    def __str__(self) -> str:
        return '\'{}\' - {} - {} - \'{}\''.format(self.old_text_hash, self.action, self.position, self.character)


class Action(Enum):
    """
    An enum defining all possible actions which can be applied to the text
    """
    UNDEFINED = 0
    ADD = 1
    REMOVE = 2
