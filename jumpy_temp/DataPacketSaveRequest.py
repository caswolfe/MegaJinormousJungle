import logging

from DataPacket import DataPacket
from DataPacketSaveDump import DataPacketSaveDump


class DataPacketSaveRequest(DataPacket):

    KEY_DOCUMENT = DataPacketSaveDump.KEY_DOCUMENT

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

        self.document: str = None

    def get_document(self) -> str:
        return self.data_dict.get(self.KEY_DOCUMENT)

    def set_document(self, document: str):
        self.data_dict.update({self.KEY_DOCUMENT: document})

    # def define_manually(self, document: str):
    #     self.document = document
    #     self.update_data_dict()

    # def update_data_dict(self) -> None:
    #     super().update_data_dict()
    #     self.data_dict.update({'document': self.document})
