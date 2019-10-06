from src.DataPacket import DataPacket


class DataPacketCursorUpdate(DataPacket):

    def __init__(self):
        super.__init__()
        pass

    def get_cursor_position(self) -> int:
        pass

    def get_is_highlighted(self) -> bool:
        pass

    def get_highlighted_pos(self) -> (int, int):
        pass
