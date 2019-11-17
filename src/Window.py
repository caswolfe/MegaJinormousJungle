import logging
from tkinter import *
from tkinter import filedialog, messagebox


# try:
#     from src.DataPacketDocumentEdit import DataPacketDocumentEdit, Action
#     from src.NetworkActionHandler import NetworkActionHandler
#     from src.NetworkHandler import NetworkHandler
# except ImportError as ie:
#     try:
#         # TODO: linux imports
from DataPacketDocumentEdit import DataPacketDocumentEdit, Action
from NetworkActionHandler import NetworkActionHandler
from NetworkHandler import NetworkHandler
from NetworkActionQueue import ActionQueue
from PySyntaxHandler import Syntax
        
    # except ImportError as ie2:
    #     print('cant import???')
    #     exit(-1)

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
        self.menu_file.add_command(label="Save", command=self.save_file)

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

    def save_file(self) -> None:
        f = filedialog.asksaveasfilename(defaultextension=".py")
        to_save_file = open(f, 'w')
        to_save_file.write(self.text.get("1.0", END))
        to_save_file.close()
        messagebox.showinfo('penis', "is saved")

    def edit(self):
        pass

    def update_text(self, action: Action, position: int, character: str, q: ActionQueue):
        self.log.debug('updating text with action: \'{}\', position: \'{}\', character: \'{}\''.format(action, position, repr(character)))
        text_current = self.text.get("1.0", END)
        text_new = text_current[1:position+1] + character + text_current[position+1:]
        self.log.debug(f"current text:{repr(text_current)} \n updated text {repr(text_new)}")
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

    def set_text(self, new_text: str):
        """
        Sets the text on the Text object directly.
        Author: Chad
        Args: new_text: string
        Returns: 
        """
        self.text.delete("1.0", END)
        self.text.insert("1.0", new_text)

    def keypress_handler(self, event):
        """
        Interpret keypresses on the local machine and send them off to be processed as
        a data packet. Keeps track of one-edit lag.
        TODO: Don't interpret all keypress as somthing to be sent e.g. don't send _alt_
        Authors: Chad, Ben
        Args: event: str unused?
        Returns:
        Interactions: sends DataPacketDocumentEdit
        """
        if self.net_hand.is_connected:
            new_text = self.text.get("1.0", END)
            packet = DataPacketDocumentEdit(old_text=self.old_text, new_text=new_text)
            if packet.character == '' or new_text == self.old_text:
                return
            else:
                self.net_hand.send_packet(packet)
        self.syntax_highlighting()
        self.old_text = self.text.get("1.0", END)

    def syntax_highlighting(self, lang = 'python'):
        """
        Highlights key elements of syntax with a color as defined in the 
        language's SyntaxHandler. Only 'python' is currently implemented,   
        but more can easily be added in the future.
        Author: Ben
        Args: lang: string, which language to use
        Returns: 

        TODO: fix so keywords inside another keyword aren't highlighted
        TODO: make so that it doesn't trigger after every character
        TODO: run on seperate thread at interval or trigger (perhaps at spacebar? would reduce work)
        """
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)
        if lang == 'python':
            SyntaxHandler = Syntax()

        syntax_dict = SyntaxHandler.get_color_dict()
        for kw in SyntaxHandler.get_keywords():
            idx = '1.0'
            color = syntax_dict[kw]
            self.text.tag_config(color, foreground=color)
           # search_term =#rf'\\y{kw}\\y'   # ' '+ kw + ' '
            while idx:
                idx = self.text.search('\\y' + kw +'\\y', idx, nocase=1, stopindex=END, regexp=True)
                if idx:
                    #self.log.debug(idx)    
                    nums = idx.split('.')
                    nums = [int(x) for x in nums]
                    #self.log.debug(f"{left} { right}")
                    lastidx = '%s+%dc' % (idx, len(kw))
                    self.text.tag_add(color, idx, lastidx)
                    idx = lastidx
            


    def get_words(self):
        """
        Gets all words (definition: seperated by a space character) in the
        Text object.
        Author: Ben
        Args: 
        Returns: words: list a list a words in the Text object
        """
        words = self.text.get("1.0", END).split(" ")
        return words
        