import json
import logging
import uuid

try:
    from src.DataPacket import DataPacket
    from src.DataPacketDocumentEdit import Action
    from src import Window
except ImportError as ie:
    try:
        # TODO: linux imports
        pass
    except ImportError as ie2:
        print('cant import???')
        exit(-1)

class NetworkActionHandler:
    
    queue = None

    def __init__(self, window: Window):
        self.window = window
        self.log = logging.getLogger('jumpy')
        self.mac = hex(uuid.getnode())

    def parse_message(self, packet: DataPacket):
        data_dict = json.loads(packet)
        packet_name = data_dict.get('packet-name')
        if data_dict.get('mac-addr') == self.mac:
            self.log.debug('received packet from self, ignoring...')
        else:
            if packet_name == 'DataPacket':
                self.log.debug('Received a DataPacket')
            elif packet_name == 'DataPacketDocumentEdit':
                self.log.debug('Received a DataPacketDocumentEdit')
                action_str = data_dict.get('action')
                position_str = data_dict.get('position')
                character_str = data_dict.get('character')
                action = Action(int(action_str))
                position = int(position_str)
                self.window.update_text(action, position, character_str)
            else:
                self.log.warning('Unknown packet type: \'{}\''.format(packet_name))
