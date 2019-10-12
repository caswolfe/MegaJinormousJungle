import threading
import socket


class Client(threading.Thread):

    def __init__(self, should_stop_func):
        super().__init__()
        self.should_stop_func = should_stop_func
        self.should_stop = self.should_stop_func()
        self.do_run = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = '10.0.2.15'
        self.port = '13000'
        self.sock.settimeout(1)

    def run(self):

        print('starting client')

        try:
            self.sock.connect((self.ip, int(self.port)))
        except ConnectionRefusedError as cre:
            print('connection refused...')
            self.should_stop = True

        while not self.should_stop:
            try:
                data = self.sock.recvfrom(1024)
                print('Client Received: {}'.format(data.decode()))
            except socket.timeout:
                print('client timeout')

            self.should_stop = self.should_stop_func()

        print('Client Fin')

        self.sock.close()

    def send_message(self, message: str):
        self.sock.sendto(message.encode(),(self.ip,self.port))
