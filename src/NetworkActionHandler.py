from src.DataPacket import DataPacket
from src.DataPacketDocumentEdit import DataPacketDocumentEdit


class NetworkActionHandler():
    
    queue = None

    def __init__(self):
        pass

    def parse_packet(self, packet: DataPacket):

        if isinstance(packet, DataPacketDocumentEdit):
            ptp = DataPacketDocumentEdit(packet)
            print(ptp)
