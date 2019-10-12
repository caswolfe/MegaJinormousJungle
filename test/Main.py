import tkinter as tk

from Server import Server
from Client import Client


class Main:

    def __init__(self):
        self.should_stop = False
        self.server = Server(should_stop_func=self.get_should_stop)
        self.client = Client(should_stop_func=self.get_should_stop)
        self.root = tk.Tk()

    def get_should_stop(self):
        return self.should_stop

    def on_exit(self):
        self.should_stop = True

        try:
            self.server.join()
        except RuntimeError as re:
            print('on_exit Runtime Error joining server thread')

        try:
            self.client.join()
        except RuntimeError as re:
            print('on_exit Runtime Error joining client thread')

        self.root.destroy()

    def func_start_server(self):
        self.server.start()

    def func_close_server(self):
        self.server.should_stop = True

    def func_join_server(self):
        self.client.start()

    def func_leave_server(self):
        self.client.should_stop = True

    def key(self, event):
        # print("pressed", repr(event.char))
        # TODO: make sure that the characters are ASCII
        self.client.send_message('key pressed: {}'.format(repr(event.char)))

    def go(self):

        self.root.title('title')

        b_stop = tk.Button(self.root, text='Stop', command=self.on_exit)
        b_stop.pack()

        # b_start_server = tk.Button(self.root, text='Open For Connection', command=self.func_start_server())
        # b_start_server.pack()
        #
        # b_start_client = tk.Button(self.root, text='Start Client', command=self.client.start)
        # b_start_client.pack()

        b_open_server = tk.Button(self.root, text='Open For Connection (Start Server)', command=self.func_start_server)
        b_close_server = tk.Button(self.root, text='Close Server (Stop Server)', command=self.func_close_server)
        b_join_server = tk.Button(self.root, text='Join Server (Start Client)', command=self.func_join_server)
        b_leave_server = tk.Button(self.root, text='Leave Server (End Client)', command=self.func_leave_server)

        b_open_server.pack()
        b_close_server.pack()
        b_join_server.pack()
        b_leave_server.pack()

        text_panel = tk.Text(self.root)
        text_panel.pack()

        self.root.bind("<Key>", self.key)

        self.root.mainloop()


if __name__ == '__main__':
    temp = Main()
    temp.go()
