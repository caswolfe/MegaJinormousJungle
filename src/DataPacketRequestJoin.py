import logging
from DataPacket import DataPacket
from DataPacketNameBroadcast import DataPacketNameBroadcast


class DataPacketRequestJoin(DataPacket):

    KEY_NAME = DataPacketNameBroadcast.KEY_NAME

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

    def get_name(self) -> str:
        return self.data_dict.get(self.KEY_NAME)

    def set_name(self, name: str):
        self.data_dict.update({self.KEY_NAME: name})
