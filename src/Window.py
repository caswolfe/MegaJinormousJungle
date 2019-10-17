from tkinter import *
from tkinter import filedialog


class Window:
    """
    This class handles all display aspects of Jum.py.
    """

    root = Tk()
    text = Text(root) 
    currentFile = None
    menu = Menu(root)
    fileMenu = Menu(menu, tearoff = 0)

    def __init__(self):

        self.create()

        self.show()

    def create(self) -> None:
        """
        Creates the window.
        """
        self.root.title("Untitled")
        self.fileMenu.add_command(label="open", command = self.openFile)
        self.text.pack()

    def show(self) -> None:
        """
        Shows the window.
        """
        self.text.mainloop()

    def open_file(self) -> None:
        """
        Prompts the user to open a file.
        """
        f = filedialog.askopenfilename(defaultextension=".txt",)
        print(f)
        if f is None or f == "":
            self.currentFile = None
        else:
            self.currentFile = f
            self.text.delete(1.0, END)
            f = open(self.currentFile, "r")
            self.text.insert(1.0, f.read())
            f.close()


if __name__ == "__main__":
    w = Window()
    # w.open_file()
    # w.show()