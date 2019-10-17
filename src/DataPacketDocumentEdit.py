import DataPacket
import datetime

class DataPacketDocumentEdit():

    def __init__(self):
        super.__init__()
        pass

    """ 
    Gets the current time of the edit. Always called before an edit
    Args:
        None
    Returns:
        ts: a timestamp
    """
    def get_time(self) -> float:
        return datetime.datetime()

    def get_edit_pos(self) -> int:
        pass

    def get_edit_char(self, line_number, col_number) -> str:
        pass


    """
    Gets the string representation of the text currently being edited
    Args:
        window: the window object
    Returns:
        doc: string representation of the document
    """
    def get_document_string(self, window)
        return window.get()