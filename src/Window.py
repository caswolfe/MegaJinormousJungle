import logging
from tkinter import *
from tkinter import filedialog

try:
    from src.DataPacketDocumentEdit import DataPacketDocumentEdit, Action
    from src.NetworkActionHandler import NetworkActionHandler
    from src.NetworkHandler import NetworkHandler
except ImportError as ie:
    try:
        # TODO: linux imports
        from DataPacketDocumentEdit import DataPacketDocumentEdit, Action
        from NetworkActionHandler import NetworkActionHandler
        from NetworkHandler import NetworkHandler
    except ImportError as ie2:
        print('cant import???')
        exit(-1)

class Window:
    """
    This class handles all display aspects of Jum.py.
    """

    # tk root
    root = Tk()

    # menu bar
    menu_bar = Menu()

    # file sub-menu in the menu bar
    menu_file = Menu(tearoff=False)

    # connections sub-menu in the menu bar
    menu_connections = Menu(tearoff=False)

    text = Text(root)

    currentFile = None

    old_text = ""

    def __init__(self):

        self.net_hand = NetworkHandler()
        self.nah = NetworkActionHandler(self)
        self.net_hand.add_network_action_handler(self.nah)

        self.log = logging.getLogger('jumpy')

        self.create()

    def create(self) -> None:
        """
        Creates the window.
        """

        self.root.title("Untitled")

        # menu bar
        self.menu_bar.add_cascade(label='File', menu=self.menu_file)
        self.menu_bar.add_cascade(label='Connections', menu=self.menu_connections)

        # file sub-menu
        self.menu_file.add_command(label="Open", command=self.open_file)

        # connections sub-menu
        self.menu_connections.add_command(label='Connect', command=self.net_hand.establish_connection)
        self.menu_connections.add_command(label='Disconnect', command=self.net_hand.close_connection)

        # cleanup
        self.root.config(menu=self.menu_bar)
        self.text.pack()
        self.text.bind_all('<Key>', self.keypress_handler)
        self.old_text = self.text.get("1.0", END)

    def show(self) -> None:
        """
        Shows the window.
        """
        self.root.mainloop()

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

    def edit(self):
        pass

    def update_text(self, action: Action, position: int, character: str):
        self.log.debug('updating text with action: \'{}\', position: \'{}\', character: \'{}\''.format(action, position, repr(character)))
        text_current = self.text.get("1.0", END)
        text_new = text_current[1:position+1] + character + text_current[position+1:]
        self.log.debug(f"current text:{text_current} \n updated text {text_new}")
        self.text.delete("1.0", END)
        self.text.insert("1.0", text_new)
        # n = 1
        # if action == Action.ADD:
        #     # TODO: fix#
        #     #
        #     text_new = character
        #     if text_new == "\n":
        #         n+=1
        #     self.log.debug("%d.%d"%(n,position))
        #     #self.text.insert("%d.%d"%(n,position), text_new)
        # elif action == Action.REMOVE:
        #     # TODO: implement
        #     pass

    def keypress_handler(self, event):
        """
        This needs to be fixed. currently the text is updated after this keypress is registered, and therefore
        the updating is allways a character beind.
        """
        if self.net_hand.is_connected:
            packet = DataPacketDocumentEdit(old_text=self.old_text, new_text=self.text.get("1.0", END))
            self.net_hand.send_packet(packet)

        self.old_text = self.text.get("1.0", END)

