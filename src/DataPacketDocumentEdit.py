import difflib
import hashlib
from enum import Enum
import logging
import json


from DataPacket import DataPacket


class DataPacketDocumentEdit(DataPacket):

    KEY_DOCUMENT = 'document'
    KEY_TEXT = 'text'

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

    def get_text(self):
        return self.data_dict.get(self.KEY_TEXT)

    def get_document(self):
        return self.data_dict.get(self.KEY_DOCUMENT)

    def set_text(self, text: str):
        self.data_dict.update({self.KEY_TEXT: text})

    def set_document(self, document: str):
        self.data_dict.update({self.KEY_DOCUMENT: document})

    # @staticmethod
    # def generate_first_change_packet(old_text: str, new_text: str, document: str):
    #     """
    #     Generates a DataPacketDocumentEdit off of the first difference between the two text's
    #
    #     :param old_text: the old text
    #     :param new_text: the new text (with changes)
    #     :param document: the document which these packets will apply to
    #
    #     :return: a single DataPacketDocumentEdit with the first detected change
    #     """
    #
    #     old_text_hash = DataPacketDocumentEdit.get_text_hash(old_text)
    #     to_ret_packet: DataPacketDocumentEdit = DataPacketDocumentEdit(document)
    #     for i, s in enumerate(difflib.ndiff(old_text, new_text)):
    #         if s[0] == ' ':
    #             pass
    #         elif s[0] == '-':
    #             action = Action.REMOVE
    #             position = i
    #             character = s[-1]
    #             to_ret_packet.define_manually(document, old_text_hash, action, position, character)
    #             return to_ret_packet
    #         elif s[0] == '+':
    #             action = Action.ADD
    #             position = i
    #             character = s[-1]
    #             to_ret_packet.define_manually(document, old_text_hash, action, position, character)
    #             return to_ret_packet
    #     return None

    # @staticmethod
    # def apply_packet_data_dict(packet_hash, packet_action, packet_positon, packet_character, current_hash, text) -> str:
    #     if packet_hash == current_hash:
    #         # if packet.data_dict.get('Action') == 1:
    #         #     return text[:packet.data_dict.get('position')] + packet.data_dict.get('character') + text[packet.data_dict.get('position'):]
    #         # elif packet.data_dict.get('Action') == 2:
    #         #     return text[:packet.data_dict.get('position')] + text[packet.data_dict.get('position')+1:]
    #         # else:
    #         #     exit(-69)
    #         if packet_action == 1:
    #             return text[:packet_positon] + packet_character + text[packet_positon:]
    #         elif packet_action == 2:
    #             return text[:packet_positon] + text[packet_positon+1:]
    #         else:
    #             exit(-69)
    #     else:
    #         raise Exception("Hash Mismatch")


class Action(Enum):
    """
    An enum defining all possible actions which can be applied to the text
    """
    UNDEFINED = 0
    ADD = 1
    REMOVE = 2
