import json
import unittest
import logging
import sys
sys.path.append("../src/")
from DataPacket import DataPacket


class Helper:

    def __init__(self):
        self.packet_received_data_dict = None

    def parse_message(self, packet_str: DataPacket):
        self.packet_received_data_dict = json.loads(packet_str)


class MyTestCase(unittest.TestCase):

    @staticmethod
    def test_NWK_08():
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
        from Window import Window
        import time

        window = Window()
        window.net_hand.unit_testing = True
        window.net_hand.establish_connection()
        time.sleep(1)
        assert window.net_hand.is_connected

        window.net_hand.close_connection()
        assert not window.net_hand.is_connected

    @staticmethod
    def test_NWK_09():
        """
        Tests the basic network functionality using the NetworkHandler
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
        from NetworkHandler import NetworkHandler
        import time
    
        # base setup
        net_hand = NetworkHandler(None)
        net_hand.unit_testing = True
        net_hand.establish_connection()
    
        time.sleep(1)
    
        net_hand.close_connection()

    @staticmethod
    def test_NWK_10():
        """
        Tests a DataPacket
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
        from DataPacket import DataPacket
        from NetworkHandler import NetworkHandler
        import time

        helper = Helper()

        # base setup
        net_hand = NetworkHandler(helper.parse_message)
        net_hand.establish_connection()
    
        time.sleep(1)
    
        assert net_hand.is_connected
    
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
    
        net_hand.send_packet(packet)
        time.sleep(1)
        net_hand.close_connection()
        assert helper.packet_received_data_dict is not None
        pass

    @staticmethod
    def test_NWK_11():
        """
        Tests a DataPacketRequestJoin
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
    
        # imports needed for this test
        from DataPacketRequestJoin import DataPacketRequestJoin
        from NetworkHandler import NetworkHandler
        import time
        helper = Helper()

        # base setup
        net_hand = NetworkHandler(helper.parse_message)
        net_hand.establish_connection()
    
        time.sleep(1)
    
        assert net_hand.is_connected
    
        packet: DataPacketRequestJoin = DataPacketRequestJoin()
        assert packet.data_dict.keys().__contains__('packet-name')
        assert packet.data_dict.keys().__contains__('mac-addr')
        assert packet.data_dict.keys().__contains__('time-of-creation')
        assert not packet.data_dict.keys().__contains__('time-of-send')
    
        assert packet.data_dict.get('packet-name').__eq__('DataPacketRequestJoin')
        assert packet.data_dict.get('mac-addr') is not None
        assert packet.data_dict.get('time-of-creation') is not None
    
        packet.set_time_of_send()
        assert packet.data_dict.keys().__contains__('time-of-send')
        assert packet.data_dict.get('time-of-send') is not None
    
        net_hand.send_packet(packet)
        time.sleep(1)
        net_hand.close_connection()
        assert helper.packet_received_data_dict is not None
        pass

    @staticmethod
    def test_NWK_12():
        """
        Tests a DataPacketRequestResponse
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
    
        # imports needed for this test
        from DataPacketRequestResponse import DataPacketRequestResponse
        from NetworkHandler import NetworkHandler
        import time
        helper = Helper()

        # base setup
        net_hand = NetworkHandler(helper.parse_message)
        net_hand.establish_connection()
    
        time.sleep(1)
    
        assert net_hand.is_connected
    
        packet: DataPacketRequestResponse = DataPacketRequestResponse()
        assert packet.data_dict.keys().__contains__('packet-name')
        assert packet.data_dict.keys().__contains__('mac-addr')
        assert packet.data_dict.keys().__contains__('time-of-creation')
        assert not packet.data_dict.keys().__contains__('time-of-send')
    
        assert packet.data_dict.get('packet-name').__eq__('DataPacketRequestResponse')
        assert packet.data_dict.get('mac-addr') is not None
        assert packet.data_dict.get('time-of-creation') is not None
    
        packet.set_time_of_send()
        assert packet.data_dict.keys().__contains__('time-of-send')
        assert packet.data_dict.get('time-of-send') is not None
    
        net_hand.send_packet(packet)
        time.sleep(1)
        net_hand.close_connection()
        assert helper.packet_received_data_dict is not None
        pass

    @staticmethod
    def test_NWK_13():
        """
        Tests a DataPacketDocumentEdit
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

        # imports needed for this test
        from DataPacketDocumentEdit import DataPacketDocumentEdit, Action

        # test a single character change
        document: str = "sample_document"
        text: str = "this is a test"
        packet: DataPacketDocumentEdit = DataPacketDocumentEdit()
        packet.set_document(document)
        packet.set_text(text)
        assert packet.get_document() == document
        assert packet.get_text() == text

        # test JSON loading and unloading
        packet_json = packet.get_json()
        packet_json_loaded = DataPacketDocumentEdit()
        packet_json_loaded.parse_json(packet_json)
        assert packet.__eq__(packet_json_loaded)

    @staticmethod
    def test_NWK_14():
        """
        Tests a DataPacketCursorUpdate
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

        from DataPacketCursorUpdate import DataPacketCursorUpdate

        dpcu = DataPacketCursorUpdate()
        document_name = 'document'
        position = '7:11'
        dpcu.set_document(document_name)
        dpcu.set_position(position)

        log.debug("\'{}\' == \'{}\' ???".format(dpcu.get_document(), document_name))

        assert dpcu.data_dict.get(DataPacketCursorUpdate.KEY_DOCUMENT) == document_name
        assert dpcu.data_dict.get(DataPacketCursorUpdate.KEY_POSITION) == position

    @staticmethod
    def test_NWK_17():
        """
        Tests a DataPacketSaveRequest
        :return:
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

        from DataPacketSaveRequest import DataPacketSaveRequest

        packet: DataPacketSaveRequest = DataPacketSaveRequest()
        document = 'document'
        packet.set_document(document)

        assert packet.get_document() == document

    @staticmethod
    def test_NWK_18():
        """
        Tests a DataPacketSaveDump
        :return:
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

        from DataPacketSaveDump import DataPacketSaveDump

        packet: DataPacketSaveDump = DataPacketSaveDump()
        document = 'document'
        text = 'this is some text from a document\no yes it is!!!'
        packet.set_document(document)
        packet.set_text(text)

        assert packet.get_document() == document
        assert packet.get_text() == text


if __name__ == '__main__':

    unittest.main()
