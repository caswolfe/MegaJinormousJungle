import json
import logging
import uuid

from src.DataPacket import DataPacket


class NetworkActionHandler():
    
    queue = None

    def __init__(self):
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
                self.log.debug(data_dict)
            else:
                self.log.warning('Unknown packet type: \'{}\''.format(packet_name))
