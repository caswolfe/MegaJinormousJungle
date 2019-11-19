import unittest
import logging


class MyTestCase(unittest.TestCase):

    @staticmethod
    def test_NWK_8():
        """
        Tests connecting to a MQTT server using the NetworkHandler
        """

        # basic logging init
        log = logging.getLogger('jumpy')
        log_format = logging.Formatter('%(filename)s - %(lineno)d - %(levelname)s - %(message)s')
        log.setLevel(logging.DEBUG)

        # logging console init
        log_handler_console = logging.StreamHandler()
        log_handler_console.setLevel(logging.DEBUG)
        log_handler_console.setFormatter(log_format)
        log.addHandler(log_handler_console)

        # imports
        from src.Window import Window
        import time

        window = Window()
        window.net_hand.unit_testing = True
        window.net_hand.establish_connection()
        time.sleep(1)
        assert window.net_hand.is_connected

        window.net_hand.close_connection()
        assert not window.net_hand.is_connected

    # @staticmethod
    # def test_NWK_9():
    #     """
    #     Tests the basic network functionality using the NetworkHandler
    #     """
    #
    #     # basic logging init
    #     log = logging.getLogger('jumpy')
    #     log_format = logging.Formatter('%(filename)s - %(lineno)d - %(levelname)s - %(message)s')
    #     log.setLevel(logging.DEBUG)
    #
    #     # logging console init
    #     log_handler_console = logging.StreamHandler()
    #     log_handler_console.setLevel(logging.DEBUG)
    #     log_handler_console.setFormatter(log_format)
    #     log.addHandler(log_handler_console)
    #
    #     # imports
    #     from src.NetworkHandler import NetworkHandler
    #     from src.NetworkActionHandler import NetworkActionHandler
    #     import time
    #
    #     # base setup
    #     net_hand = NetworkHandler()
    #     net_hand.unit_testing = True
    #     net_hand.establish_connection()
    #
    #     time.sleep(1)
    #
    #     # testing add and rem of NetworkActionHandler to a NetworkHandler
    #     len_of_nahs = len(net_hand.nahs)
    #     nah = NetworkActionHandler(None)
    #     net_hand.add_network_action_handler(nah)
    #     assert len(net_hand.nahs) == len_of_nahs + 1
    #     net_hand.remove_network_action_handler(nah)
    #     assert len(net_hand.nahs) == len_of_nahs
    #
    #     net_hand.close_connection()

    # @staticmethod
    # def test_NWK_10():
    #     """
    #     Tests a DataPacket
    #     """
    #
    #     # basic logging init
    #     log = logging.getLogger('jumpy')
    #     log_format = logging.Formatter('%(filename)s - %(lineno)d - %(levelname)s - %(message)s')
    #     log.setLevel(logging.DEBUG)
    #
    #     # logging console init
    #     log_handler_console = logging.StreamHandler()
    #     log_handler_console.setLevel(logging.DEBUG)
    #     log_handler_console.setFormatter(log_format)
    #     log.addHandler(log_handler_console)
    #
    #     # imports
    #     from src.DataPacket import DataPacket
    #     from src.NetworkHandler import NetworkHandler
    #     import time
    #
    #     # base setup
    #     net_hand = NetworkHandler()
    #     net_hand.establish_connection()
    #
    #     time.sleep(1)
    #
    #     assert net_hand.is_connected
    #
    #     packet: DataPacket = DataPacket()
    #     assert packet.data_dict.keys().__contains__('packet-name')
    #     assert packet.data_dict.keys().__contains__('mac-addr')
    #     assert packet.data_dict.keys().__contains__('time-of-creation')
    #     assert not packet.data_dict.keys().__contains__('time-of-send')
    #
    #     assert packet.data_dict.get('packet-name').__eq__('DataPacket')
    #     assert packet.data_dict.get('mac-addr') is not None
    #     assert packet.data_dict.get('time-of-creation') is not None
    #
    #     packet.set_time_of_send()
    #     assert packet.data_dict.keys().__contains__('time-of-send')
    #     assert packet.data_dict.get('time-of-send') is not None
    #
    #     net_hand.send_packet(packet)
    #     time.sleep(1)
    #     net_hand.close_connection()
    #     assert net_hand.unit_testing_received_packet is not None
    #     pass

    # @staticmethod
    # def test_NWK_11():
    #     """
    #     Tests a DataPacketRequestJoin
    #     """
    #     assert 1 == 1

    # @staticmethod
    # def test_NWK_12():
    #     """
    #     Tests a DataPacketRequestResponse
    #     """
    #     assert 1 == 1

    # @staticmethod
    # def test_NWK_13():
    #     """
    #     Tests a DataPacketDocumentEdit
    #     """
    #
    #     # basic logging init
    #     log = logging.getLogger('jumpy')
    #     log_format = logging.Formatter('%(filename)s - %(lineno)d - %(levelname)s - %(message)s')
    #     log.setLevel(logging.DEBUG)
    #
    #     # logging console init
    #     log_handler_console = logging.StreamHandler()
    #     log_handler_console.setLevel(logging.DEBUG)
    #     log_handler_console.setFormatter(log_format)
    #     log.addHandler(log_handler_console)
    #
    #     # imports needed for this test
    #     from src.DataPacketDocumentEdit import DataPacketDocumentEdit, Action
    #
    #     # test a single character change
    #     old_text: str = "this is a tes"
    #     new_text: str = "this is a test"
    #     packet: DataPacketDocumentEdit = DataPacketDocumentEdit.generate_first_change_packet(old_text, new_text, 'test_doc')
    #     assert packet.check_hash(old_text)
    #     assert packet.action == Action.ADD
    #     assert packet.position == 13
    #     assert packet.character == 't'
    #
    #     # test the application of a packet to a string
    #     applied_text: str = DataPacketDocumentEdit.apply_packet(old_text, packet)
    #     assert applied_text == new_text
    #
    #     # test JSON loading and unloading
    #     packet_json = packet.get_json()
    #     packet_json_loaded = DataPacketDocumentEdit('test_doc')
    #     packet_json_loaded.parse_json(packet_json)
    #     assert packet.__eq__(packet_json_loaded)
    #
    #     # test a multiple character change
    #     old_text: str = "this is a"
    #     new_text: str = "this is a test"
    #     packets: list[DataPacketDocumentEdit] = DataPacketDocumentEdit.generate_packets_from_changes(old_text, new_text, 'test_doc')
    #     applied_text = DataPacketDocumentEdit.apply_multiple_packets(old_text, packets)
    #     assert applied_text == new_text

    # @staticmethod
    # def test_NWK_14():
    #     """
    #     Tests a DataPacketCursorUpdate
    #     """
    #     assert 1 == 1

    # @staticmethod
    # def test_NWK_15():
    #     """
    #     Tests a DataPacketMsg
    #     """
    #     assert 1 == 1

    # @staticmethod
    # def test_NWK_16():
    #     """
    #     Tests a DataPacketLeaveLobby
    #     """
    #     assert 1 == 1


if __name__ == '__main__':

    unittest.main()
