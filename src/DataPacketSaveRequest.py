import logging

from DataPacket import DataPacket


class DataPacketSaveRequest(DataPacket):

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

        self.document: str = None

    def define_manually(self, document: str):
        self.document = document
        self.update_data_dict()

    def update_data_dict(self) -> None:
        super().update_data_dict()
        self.data_dict.update({'document': self.document})
