import logging

try:
    from src.DataPacket import DataPacket, DataPacketDocumentEdit
except ImportError as ie:
    try:
        # TODO: linux imports
        from DataPacket import DataPacket, DataPacketDocumentEdit
    except ImportError as ie2:
        print('cant import???')
        exit(-1)


class DataPacketSaveDump(DataPacket):

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

        self.document: str = None
        self.text_hash: str = None
        self.text: str = None

    def define_manually(self, document: str, text: str):
        # TODO: discuss if we should compress the text
        self.document = document
        self.text_hash = DataPacketDocumentEdit.get_text_hash(text)
        self.text = text
        self.update_data_dict()

    def update_data_dict(self) -> None:
        super().update_data_dict()
        self.data_dict.update({'document': self.text_hash})
        self.data_dict.update({'text_hash': self.text_hash})
        self.data_dict.update({'text': self.text})
