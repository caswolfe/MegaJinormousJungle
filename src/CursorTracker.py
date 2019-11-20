from tkinter import *
from tkinter import filedialog, messagebox
from time import sleep


class CursorTracker:

    def __init__(self, window):
        self.window = window
        self.text = window.text
        self.root = window.root
        self.run = True

    def track_cursor(self, window):
        while self.run:
            position = self.text.index(INSERT)
            # send position of cursor to others
            sleep(1)
