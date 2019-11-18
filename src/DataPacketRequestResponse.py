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
