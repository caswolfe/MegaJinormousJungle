import unittest


class MyTestCase(unittest.TestCase):

    def test_NWK_8(self):
        """
        Tests connecting to a MQTT server using the NetworkHandler
        """

        from src.NetworkHandler import NetworkHandler

        nh: NetworkHandler = NetworkHandler()
        nh.establish_connection()
        assert nh.is_connected

        nh.close_connection()
        assert not nh.is_connected

    # def test_NWK_9(self):
    #     """
    #     Tests the basic network functionality using the NetworkHandler
    #     """
    #     assert 1 == 1

    def test_NWK_10(self):
        """
        Tests a DataPacket
        """

        # imports
        from src.DataPacket import DataPacket

        packet: DataPacket = DataPacket()
        assert packet.data_dict.keys().__contains__('packet-name')
        assert packet.data_dict.keys().__contains__('mac-addr')
        assert packet.data_dict.keys().__contains__('time-of-creation')
        assert not packet.data_dict.keys().__contains__('time-of-send')

        assert packet.data_dict.get('packet-name').__eq__('DataPacket')
        assert packet.data_dict.get('mac-addr') is not None
        assert packet.data_dict.get('time-of-creation') is not None

        packet.set_time_of_send()
        assert packet.data_dict.keys().__contains__('time-of-send')
        assert packet.data_dict.get('time-of-send') is not None

    # def test_NWK_11(self):
    #     """
    #     Tests a DataPacketRequestJoin
    #     """
    #     assert 1 == 1

    # def test_NWK_12(self):
    #     """
    #     Tests a DataPacketRequestResponse
    #     """
    #     assert 1 == 1

    @staticmethod
    def test_NWK_13():
        """
        Tests a DataPacketDocumentEdit
        """

        # imports needed for this test
        from src.DataPacketDocumentEdit import DataPacketDocumentEdit, Action

        # test a single character change
        old_text: str = "this is a tes"
        new_text: str = "this is a test"
        packet: DataPacketDocumentEdit = DataPacketDocumentEdit.generate_first_change_packet(old_text, new_text, 'test_doc')
        assert packet.check_hash(old_text)
        assert packet.action == Action.ADD
        assert packet.position == 13
        assert packet.character == 't'

        # test the application of a packet to a string
        applied_text: str = DataPacketDocumentEdit.apply_packet(old_text, packet)
        assert applied_text == new_text

        # test JSON loading and unloading
        packet_json = packet.get_json()
        packet_json_loaded = DataPacketDocumentEdit('test_doc')
        packet_json_loaded.parse_json(packet_json)
        assert packet.__eq__(packet_json_loaded)

        # test a multiple character change
        old_text: str = "this is a"
        new_text: str = "this is a test"
        packets: list[DataPacketDocumentEdit] = DataPacketDocumentEdit.generate_packets_from_changes(old_text, new_text, 'test_doc')
        applied_text = DataPacketDocumentEdit.apply_multiple_packets(old_text, packets)
        assert applied_text == new_text

    # def test_NWK_14(self):
    #     """
    #     Tests a DataPacketCursorUpdate
    #     """
    #     assert 1 == 1

    # def test_NWK_15(self):
    #     """
    #     Tests a DataPacketMsg
    #     """
    #     assert 1 == 1

    # def test_NWK_16(self):
    #     """
    #     Tests a DataPacketLeaveLobby
    #     """
    #     assert 1 == 1


if __name__ == '__main__':
    unittest.main()
