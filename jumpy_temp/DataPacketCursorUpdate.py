import logging

from DataPacket import DataPacket
from DataPacketSaveDump import DataPacketSaveDump


class DataPacketCursorUpdate(DataPacket):

    KEY_DOCUMENT = DataPacketSaveDump.KEY_DOCUMENT
    KEY_POSITION = 'position'

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

    def get_document(self):
        self.data_dict.get(self.KEY_DOCUMENT)

    def get_position(self):
        self.data_dict.get(self.KEY_POSITION)

    def set_document(self, document: str):
        self.data_dict.update({self.KEY_DOCUMENT: document})

    def set_position(self, position: int):
        self.data_dict.update({self.KEY_POSITION: position})

    # def define_manually(self, document: str, positon: str):
    #     self.document = document
    #     self.position = positon
    #     self.update_data_dict()

    # def update_data_dict(self) -> None:
    #     super().update_data_dict()
    #     self.data_dict.update({'document': self.document})
    #     self.data_dict.update({'position': self.position})
