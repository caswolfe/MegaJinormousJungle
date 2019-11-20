import logging

from DataPacket import DataPacket


class DataPacketRequestResponse(DataPacket):

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

        self.target_mac: str = None
        self.can_join: bool = None

    def define_manually(self, target_mac: str, can_join: bool):
        self.target_mac = target_mac
        self.can_join = can_join

    def update_data_dict(self) -> None:
        super().update_data_dict()
        self.data_dict.update({'target_mac': self.target_mac})
        self.data_dict.update({'can_join': self.can_join})
