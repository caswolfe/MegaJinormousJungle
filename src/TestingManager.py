try:
    from src.DataPacket import DataPacket
    from src.DataPacketDocumentEdit import Action
    from src import Window
    from src.NetworkActionHandler import NetworkActionHandler
    from src.NetworkHandler import NetworkHandler
except ImportError as ie:
    try:
        # TODO: linux imports
        from DataPacket import DataPacket
        from DataPacketDocumentEdit import Action
        from Window import Window
        from NetworkActionHandler import NetworkActionHandler
        from NetworkHandler import NetworkHandler
    except ImportError as ie2:
        print('cant import???')
        exit(-1)

import unittest


class testConnection(unittest.TestCase):
    def setup(self):
        pass

    """
    Test creation of window
    """
    def testA(self):
        self.window = Window()
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
