from tkinter import *


class CursorUpdater:

    def __init__(self, window, position, file):
        #self.position = position
        #self.name = file
        self.text = window.text
        self.root = window.root
        self.set_cursor(position, "No name")

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
