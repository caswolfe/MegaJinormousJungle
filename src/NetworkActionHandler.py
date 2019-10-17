import DataPacket
from ActionQueue import ActionQueue

class NetworkActionHandler():
    
    queue = None

    def __init__(self):
        self.queue = ActionQueue()

    def parse_packet(self, packet: DataPacket) -> tuple:
        pass
