import json
import logging
import uuid
from tkinter import END

from src.DataPacket import DataPacket
from src.DataPacketDocumentEdit import Action
from src import Window


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
                self.log.debug(data_dict)
                action_str = data_dict.get('action')
                position_str = data_dict.get('position')
                character_str = data_dict.get('character')
                action = Action(int(action_str))
                position = int(position_str)
                text_current = self.window.text.get("1.0", END)
                if action == Action.ADD:
                    self.log.debug('inserting new text')
                    text_new = text_current[:position] + character_str + text_current[:position]
                    self.log.debug('old text: {}'.format(repr(text_current)))
                    self.log.debug('new text: {}'.format(repr(text_new)))
                    self.window.text.update(1.0, text_new)
            else:
                self.log.warning('Unknown packet type: \'{}\''.format(packet_name))
