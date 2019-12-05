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


class Action(Enum):
    """
    An enum defining all possible actions which can be applied to the text
    """
    UNDEFINED = 0
    ADD = 1
    REMOVE = 2
