import threading
import socket


class Server(threading.Thread):

    def __init__(self, should_stop_func):
        super().__init__()
        self.should_stop_func = should_stop_func
        self.should_stop = self.should_stop_func()
        self.sock = socket.socket()
        self.ip = '127.0.0.1'
        self.port = '12345'
        self.sock.settimeout(1)
        self.connection_list = []

    def run(self):

        print('starting server...')

        current_thread = threading.current_thread()

        self.sock.bind((self.ip, int(self.port)))

        self.sock.listen(1)

        cl = ConnectionListener(self.sock, self.get_connection_list, self.should_stop_func)
        cl.start()

        while not self.should_stop:
            # try:
            #     connection, address = self.sock.accept()
            #     print('received a connection from {}'.format(address))
            #     connection.send(b'Thank you for connecting!')
            #     connection.close()
            # except socket.timeout as to:
            #     pass

            # try:
            #     data = self.sock.recv(1024)
            #     print('Server Received: {}'.format(data))
            # except socket.timeout:
            #     print('Server timeout')

            for conn, addr in self.connection_list:
                try:
                    data = conn.recv(1024)
                    print('Server Received: {}'.format(data.decode()))
                except socket.timeout:
                    print('Server timeout')

            self.should_stop = self.should_stop_func()

        print('server stopping...')

        self.sock.close()

    def get_connection_list(self):
        return self.connection_list


class ConnectionListener(threading.Thread):

    def __init__(self, server_socket, func_get_connection_list, func_should_stop):
        super().__init__()
        self.setDaemon(True)
        self.server_socket = server_socket
        self.func_Get_connection_list = func_get_connection_list
        self.func_should_stop = func_should_stop

    def run(self) -> None:

        print("starting CL")

        while not self.func_should_stop():
            print('accepting connection')
            try:
                connection, address = self.server_socket.accept()
                self.func_Get_connection_list().append((connection, address))
                print('server received connection...')
                connection.send(b'connection received!')
            except socket.timeout as to:
                pass
        print('CL closing...')
