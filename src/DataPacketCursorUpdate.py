import logging


from DataPacket import DataPacket, DataPacketDocumentEdit



class DataPacketCursorUpdate(DataPacket):

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

        self.document: str = None
        self.position: int = None

    def define_manually(self, document: str, positon: int):
        self.document = document
        self.position = positon
        self.update_data_dict()

    def update_data_dict(self) -> None:
        super().update_data_dict()
        self.data_dict.update({'document': self.document})
        self.data_dict.update({'position': self.position})
