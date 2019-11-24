import logging

from DataPacket import DataPacket


class DataPacketRequestResponse(DataPacket):

    KEY_TARGET_MAC = 'target_mac'
    KEY_CAN_JOIN = 'can_join'

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')

        self.target_mac: str = None
        self.can_join: bool = None

    def get_target_mac(self):
        return self.data_dict.get(self.KEY_TARGET_MAC)

    def get_can_join(self) -> bool:
        return self.data_dict.get(self.KEY_CAN_JOIN)

    def set_target_mac(self, target_mac: str):
        self.data_dict.update({self.KEY_TARGET_MAC: target_mac})

    def set_can_join(self, can_join: bool):
        self.data_dict.update({self.KEY_CAN_JOIN: can_join})

    # def define_manually(self, target_mac: str, can_join: bool):
    #     self.target_mac = target_mac
    #     self.can_join = can_join

    # def update_data_dict(self) -> None:
    #     super().update_data_dict()
    #     self.data_dict.update({'target_mac': self.target_mac})
    #     self.data_dict.update({'can_join': self.can_join})
