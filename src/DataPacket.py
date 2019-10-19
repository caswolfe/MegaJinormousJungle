import uuid
import pickle
import codecs


class DataPacket:

    def __int__(self):
        self.mac = hex(uuid.getnode())

    def get_sender_mac(self) -> str:
        return self.mac

    def get_doc_hash(self) -> int:
        pass

    def get_pickle(self):
        pass


def get_packet_from_pickled_str(string: str):
    pass
