import logging
from DataPacket import DataPacket

class DataPacketRequestJoin(DataPacket):

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')
