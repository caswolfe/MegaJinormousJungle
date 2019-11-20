from DataPacket import DataPacket
from DataPacketDocumentEdit import Action
from Window import Window
from NetworkActionHandler import NetworkActionHandler
from NetworkHandler import NetworkHandler
import unittest


class testConnection(unittest.TestCase):
    def setup(self):
        pass

    """
    Test creation of window
    """
    def testA(self):
        self.window = Window.Window()
        assert self.window

    """
    Test creation of network handelers
    """
    def testB(self):
        self.net_hand = NetworkHandler()
        self.nah = NetworkActionHandler(self)
        self.net_hand.add_network_action_handler(self.nah)
        assert self.net_hand
        assert self.nah
    """
    Test connection itself
    """
    def testC(self):
        self.net_hand = NetworkHandler()
        self.nah = NetworkActionHandler(self)
        self.net_hand.add_network_action_handler(self.nah)
        self.net_hand.establish_connection()
        assert self.net_hand.is_connected
        self.net_hand.close_connection()
        assert not self.net_hand.is_connected
        

if __name__ == "__main__":
    unittest.main()
