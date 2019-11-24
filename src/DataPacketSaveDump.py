import logging

from DataPacket import DataPacket
from DataPacketDocumentEdit import DataPacketDocumentEdit


class DataPacketSaveDump(DataPacket):

    KEY_DOCUMENT = 'document'
    KEY_TEXT_HASH = 'text_hash'
    KEY_TEXT = 'text'

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

        self.document: str = None
        self.text_hash: str = None
        self.text: str = None

    def get_document(self) -> str:
        return self.data_dict.get(self.KEY_DOCUMENT)

    def get_text_hash(self) -> str:
        return self.data_dict.get(self.KEY_TEXT_HASH)

    def get_text(self) -> str:
        return self.data_dict.get(self.KEY_TEXT)

    def set_document(self, document: str):
        self.data_dict.update({self.KEY_DOCUMENT: document})

    def set_text_hash(self, text_hash: str):
        self.data_dict.update({self.KEY_TEXT_HASH: text_hash})

    def set_text(self, text: str):
        self.data_dict.update({self.KEY_TEXT: text})

    # def define_manually(self, document: str, text: str):
    #     # TODO: discuss if we should compress the text
    #     self.document = document
    #     self.text_hash = DataPacketDocumentEdit.get_text_hash(text)
    #     self.text = text
    #     self.update_data_dict()

    # def update_data_dict(self) -> None:
    #     super().update_data_dict()
    #     self.data_dict.update({'document': self.document})
    #     self.data_dict.update({'text_hash': self.text_hash})
    #     self.data_dict.update({'text': self.text})
