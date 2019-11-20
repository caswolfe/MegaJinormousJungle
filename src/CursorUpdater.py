from tkinter import *
from tkinter import filedialog, messagebox


class CursorUpdater:

    def __init__(self, window, position, name):
        self.position = position
        self.name = name
        self.text = window.text
        self.root = window.root

    def update_cursor(self):
        # get position from network
        self.set_cursor(self.position, self.name)

    def set_cursor(self, position, name):
        self.text.tag_config("cursor_tag", foreground="red")
        self.text.tag_bind("cursor_tag", "<Enter>", lambda event: self.cursor_label(event, name))
        self.text.insert(position, "|", "cursor_tag")

    def cursor_label(self, event, name):
        print("Over " + name + " cursor")
        label = Label(self.root, text="This cursor belongs to " + name)
        label.pack(fill=BOTH)

        self.text.tag_bind("cursor_tag", "<Leave>", lambda e: label.destroy())  # Remove popup when pointer leaves the window
        self.root.update()
