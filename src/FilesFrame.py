from tkinter import *
import os

class FilesFrame(Frame):

    def __init__(self, root, window):
        self.window = window
        Frame.__init__(self, root)
        self.canvas = Canvas(root,width=root.cget("width"))
        self.frame = Frame(self.canvas,borderwidth=5,bg="light grey")
        self.vsb = Scrollbar(root, orient="vertical",bg="grey", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right",fill="y")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_window((0,0),window=self.frame, anchor="nw", 
                                  tags="self.frame",width=root.cget("width"))

        self.frame.bind("<Configure>", self.onFrameConfigure)

    def populate(self, workspace):
        for item in workspace.files:
            item_path = workspace.directory + "/" + item
            Radiobutton(self.frame, text=item, variable=self.window.current_file_name, command=self.window.open_item, value=item_path, indicator=0).pack(side='top', fill='x', expand=True)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
