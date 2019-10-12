from tkinter import *
from tkinter import filedialog


class Window:
    root = Tk()
    text = Text(root) 
    currentFile = None
    menu = Menu(root)
    fileMenu = Menu(menu, tearoff = 0)

    def __init__(self):

        self.create()

        self.show()

    def create(self) -> None:
        self.root.title("Untitled")
        self.fileMenu.add_command(label = "open", command = self.openFile)
        self.text.pack()


    def show(self) -> None:
        self.text.mainloop()

    def openFile(self):
        f = filedialog.askopenfilename(defaultextension=".txt",)
        print(f)
        if f is None or f == "":
            self.currentFile = None
        else:
            self.currentFile = f
            self.text.delete(1.0,END) 
            f = open(self.currentFile,"r") 
            self.text.insert(1.0,f.read()) 
            f.close()

if __name__ == "__main__":
    w = Window()
    #w.openFile()
    #w.show()