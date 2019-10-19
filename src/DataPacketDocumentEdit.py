from enum import Enum

from src.DataPacket import DataPacket
from datetime import datetime
import difflib
import hashlib


class DataPacketDocumentEdit(DataPacket):

    def __init__(self, old_text: str, new_text: str):
        super().__init__()
        self.time_of_creation = datetime.now()
        self.old_text_hash = hashlib.sha1(old_text.encode()).hexdigest()
        for i, s in enumerate(difflib.ndiff(old_text, new_text)):
            if s[0] == ' ':
                self.action = Action.NONE
                self.position = -1
                self.character = ''
            elif s[0] == '-':
                self.action = Action.REMOVE
                self.position = i
                self.character = s[-1]
            elif s[0] == '+':
                self.action = Action.ADD
                self.position = i
                self.character = s[-1]

    def get_time_of_creation(self) -> float:
        return self.time_of_creation

    def get_action(self):
        return self.action

    def get_pos(self) -> int:
        return self.position

    def get_char(self) -> str:
        return self.character

    def get_old_text_hash(self):
        return self.old_text_hash

    def __str__(self) -> str:
        return '{} - {} - {} - {}'.format(self.old_text_hash, self.action, self.position, self.character)


class Action(Enum):
    NONE = ''
    ADD = '+'
    REMOVE = '-'
