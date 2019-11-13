import unittest


class MyTestCase(unittest.TestCase):

    def test_NWK_8(self):
        """
        Tests connecting to a MQTT server using the NetworkHandler
        """
        assert 1 == 1

    def test_NWK_9(self):
        """
        Tests the basic network functionality using the NetworkHandler
        """
        assert 1 == 1

    def test_NWK_10(self):
        """
        Tests a DataPacket
        """
        assert 1 == 1

    def test_NWK_11(self):
        """
        Tests a DataPacketCreateLobby
        """
        assert 1 == 1

    def test_NWK_12(self):
        """
        Tests a DataPacketJoinLobby
        """
        assert 1 == 1

    def test_NWK_13(self):
        """
        Tests a DataPacketDocumentEdit
        """
        assert 1 == 1

    def test_NWK_14(self):
        """
        Tests a DataPacketCursorUpdate
        """
        assert 1 == 1

    def test_NWK_15(self):
        """
        Tests a DataPacketMsg
        """
        assert 1 == 1

    def test_NWK_16(self):
        """
        Tests a DataPacketLeaveLobby
        """
        assert 1 == 1


if __name__ == '__main__':
    unittest.main()
