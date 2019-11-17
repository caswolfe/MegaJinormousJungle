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

        self.text_hash: str = None
        self.text: str = None

    def define_manually(self, text):
        self.text_hash = DataPacketDocumentEdit.get_text_hash(text)
        self.text = text
        self.update_data_dict()

    def update_data_dict(self) -> None:
        self.data_dict.update({'text_hash': self.text_hash})
        self.data_dict.update({'text': self.text})
