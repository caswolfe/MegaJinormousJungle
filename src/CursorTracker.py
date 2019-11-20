from tkinter import *
from tkinter import filedialog, messagebox


class CursorTracker:

    window = None

    def __init__(self, window):
        self.window = window

    text = window.text
    root = window.root

    def track_cursor(self):
        while True:
            position = self.get_cursor_position()
            # send position of cursor to others

    def get_cursor_position(self):
        position = self.text.index(INSERT)
        return position
