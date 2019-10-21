import logging
from tkinter import *
from tkinter import filedialog

from src.DataPacketDocumentEdit import DataPacketDocumentEdit, Action
from src.NetworkActionHandler import NetworkActionHandler
from src.NetworkHandler import NetworkHandler


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

    def update_text(self, packet: DataPacketDocumentEdit):
        data_dict = packet.get_json()
        action_str = data_dict.get('action')
        position_str = data_dict.get('position')
        character_str = data_dict.get('character')
        action = Action(int(action_str))
        position = int(position_str)
        text_current = self.window.text.get("1.0", END)
        if action == Action.ADD:
            self.log.debug('inserting new text')
            text_new = text_current[:position] + character_str + text_current[:position]
            self.log.debug('old text: {}'.format(repr(text_current)))
            self.log.debug('new text: {}'.format(repr(text_new)))
            self.window.text.delete(1.0, END)
            self.window.text.update(1.0, text_new)

    def keypress_handler(self, event):
        """
        This needs to be fixed. currently the text is updated after this keypress is registered, and therefore
        the updating is allways a character beind.
        """
        if self.net_hand.is_connected:
            packet = DataPacketDocumentEdit(old_text=self.old_text, new_text=self.text.get("1.0", END))
            self.net_hand.send_packet(packet)

        self.old_text = self.text.get("1.0", END)

