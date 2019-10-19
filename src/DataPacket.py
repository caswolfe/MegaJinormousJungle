import uuid


class DataPacket:

    def __int__(self, alias: str = 'UNKNOWN', lobby: str = 'GLOBAL'):
        self.alias = alias
        self.lobby = lobby
        self.mac = hex(uuid.getnode())

    def get_sender_alias(self) -> str:
        return self.alias

    def get_sender_mac(self) -> str:
        return self.mac

    def get_doc_hash(self) -> int:
        pass
