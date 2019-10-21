import difflib
import hashlib
from enum import Enum
import logging
import json

from src.DataPacket import DataPacket


class DataPacketDocumentEdit(DataPacket):

    def __init__(self, old_text: str = None, new_text: str = None, json_str: str = None):
        super().__init__()
        self.log = logging.getLogger('jumpy')
        if json_str is None:
            self.old_text_hash = hashlib.sha1(old_text.encode()).hexdigest()
            self.log.debug('{} => {}'.format(repr(old_text), repr(new_text)))
            for i, s in enumerate(difflib.ndiff(old_text, new_text)):
                if s[0] == ' ':
                    # self.action = Action.NONE
                    # self.position = -1
                    # self.character = ''
                    # self.log.debug('None')
                    pass
                elif s[0] == '-':
                    self.action = Action.REMOVE
                    self.position = i
                    self.character = s[-1]
                    self.log.debug('Delete \'{}\' from position \'{}\''.format(self.character, self.position))
                elif s[0] == '+':
                    self.action = Action.ADD
                    self.position = i
                    self.character = s[-1]
                    self.log.debug('Add \'{}\' to position \'{}\''.format(self.character, self.position))
            self.data_dict.update({'action': self.action.value})
            self.data_dict.update({'position': self.position})
            self.data_dict.update({'character': self.character})
        else:
            self.data_dict = json.loads(json_str)

    def __str__(self) -> str:
        return '{} - {} - {} - {}'.format(self.old_text_hash, self.action, self.position, self.character)


class Action(Enum):
    NONE = 0
    ADD = 1
    REMOVE = 2
