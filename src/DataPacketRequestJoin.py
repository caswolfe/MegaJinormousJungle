import logging
from DataPacket import DataPacket
from DataPacketDocumentEdit import DataPacketDocumentEdit

class DataPacketRequestJoin(DataPacket):

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger('jumpy')