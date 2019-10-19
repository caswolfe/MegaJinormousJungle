import uuid


class DataPacket:

    def __int__(self):
        self.mac = hex(uuid.getnode())

    def get_sender_mac(self) -> str:
        return self.mac

    def get_doc_hash(self) -> int:
        pass
