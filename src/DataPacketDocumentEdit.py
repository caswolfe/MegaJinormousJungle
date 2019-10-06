from src.DataPacket import DataPacket


class DataPacketDocumentEdit(DataPacket):

    def __init__(self):
        super.__init__()
        pass

    def get_time(self) -> float:
        pass

    def get_edit_pos(self) -> int:
        pass

    def get_edit_char(self) -> str:
        pass
