import difflib
import hashlib
from enum import Enum
import logging
import json


from DataPacket import DataPacket


class DataPacketDocumentEdit(DataPacket):

    def __init__(self, document: str):
        super().__init__()
        self.log = logging.getLogger('jumpy')

        # default values
        self.document: str = document
        self.old_text_hash: str = None
        self.action: Action = Action.UNDEFINED
        self.position: int = -1
        self.character: str = ''
        self.update_data_dict()

    def define_manually(self, document: str, old_text_hash, action, position: int, character: str) -> None:
        """
        Sets the parameters of the packet manually

        :param document: The document in which this change applies to
        :param old_text_hash: The hash of the old text
        :param action: The action to be applied
        :param position: The position where the action will be applied
        :param character: The character which will be applied
        """

        self.document = document
        self.old_text_hash = old_text_hash
        self.action = action
        self.position = position
        self.character = character
        self.update_data_dict()

    def update_data_dict(self) -> None:
        super().update_data_dict()
        self.data_dict.update({'document': self.document})
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
        return self.get_text_hash(text) == self.data_dict.get('old_text_hash')

    @staticmethod
    def generate_first_change_packet(old_text: str, new_text: str, document: str):
        """
        Generates a DataPacketDocumentEdit off of the first difference between the two text's

        :param old_text: the old text
        :param new_text: the new text (with changes)
        :param document: the document which these packets will apply to

        :return: a single DataPacketDocumentEdit with the first detected change
        """

        old_text_hash = hashlib.sha1(old_text.encode()).hexdigest()
        to_ret_packet: DataPacketDocumentEdit = DataPacketDocumentEdit(document)
        for i, s in enumerate(difflib.ndiff(old_text, new_text)):
            if s[0] == ' ':
                pass
            elif s[0] == '-':
                action = Action.REMOVE
                position = i
                character = s[-1]
                to_ret_packet.define_manually(document, old_text_hash, action, position, character)
                return to_ret_packet
            elif s[0] == '+':
                action = Action.ADD
                position = i
                character = s[-1]
                to_ret_packet.define_manually(document, old_text_hash, action, position, character)
                return to_ret_packet
        return None

    @staticmethod
    def generate_packets_from_changes(old_text: str, new_text: str, document: str):
        """
        generates a list of DataPacketDocumentEdit's which will allow one to alter the old_text into the new_text

        :param old_text: the old text
        :param new_text: the new text (with changes)
        :param document: the document which these packets will apply to

        :return: a list of DataPacketDocumentEdit's which can be applied to the old_text (sequentially) to bring it up to new_text
        """

        generated_packets = list()
        current_text: str = old_text
        change = DataPacketDocumentEdit.generate_first_change_packet(current_text, new_text, document)
        while change is not None:

            generated_packets.append(change)
            if change.check_hash(current_text):
                current_text = DataPacketDocumentEdit.apply_packet(current_text, change)
            else:
                raise Exception("Hash Mismatch")

            change = DataPacketDocumentEdit.generate_first_change_packet(current_text, new_text, document)

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
            return text[:packet.data_dict.get('position')] + packet.data_dict.get('character') + text[packet.data_dict.get('position'):]
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


    @staticmethod
    def apply_packet_data_dict(packet_hash, packet_positon, packet_character, current_hash, text) -> str:
        if packet_hash == current_hash:
            return text[:packet_positon] + packet_character + text[packet_positon:]
        else:
            raise Exception("Hash Mismatch")

class Action(Enum):
    """
    An enum defining all possible actions which can be applied to the text
    """
    UNDEFINED = 0
    ADD = 1
    REMOVE = 2
