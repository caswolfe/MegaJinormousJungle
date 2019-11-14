import unittest


HOST = "postman.cloudmqtt.com"
PORT = 13272
USERNAME = "jumpy-user"
PASSWORD = "password"
TOPIC = "testing"


class MQTTHelper:

    """
    Used to organize the testing suite in a more readable manner
    """

    def __init__(self, client):

        # setting up mqtt hooks
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_subscribe = self.on_subscribe
        client.on_publish = self.on_publish

        #
        # setting up variables for testing / asserting
        #

        # on_connect
        self.on_connect_last_client = None
        self.on_connect_last_userdata = None
        self.on_connect_last_flags = None
        self.on_connect_last_rc = None

        # on_message
        self.on_message_last_client = None
        self.on_message_last_userdata = None
        self.on_message_last_msg = None

        # on_subscribe
        self.on_subscribe_last_client = None
        self.on_subscribe_last_obj = None
        self.on_subscribe_last_mid = None
        self.on_subscribe_last_granted_qos = None

    def on_connect(self, client, userdata, flags, rc):
        self.on_connect_last_client = client
        self.on_connect_last_userdata = userdata
        self.on_connect_last_flags = flags
        self.on_connect_last_rc = rc

    def on_message(self, client, userdata, msg):
        self.on_message_last_client = client
        self.on_message_last_userdata = userdata
        self.on_message_last_msg = msg

    def on_subscribe(self, client, obj, mid, granted_qos):
        self.on_subscribe_last_client = client
        self.on_subscribe_last_obj = obj
        self.on_subscribe_last_mid = mid
        self.on_subscribe_last_granted_qos = granted_qos

    def on_publish(self):
        print("on_publish")


class MyTestCase(unittest.TestCase):

    @staticmethod
    def test_NWK_1():
        """
        Tests paho-mqtt importing
        """
        error = False
        try:
            import paho.mqtt.client as mqtt
        except ImportError as ie:
            error = True

        assert not error

    @staticmethod
    def test_NWK_2():
        """
        Tests connecting to an MQTT server with paho-mqtt
        """

        # imports
        import paho.mqtt.client as mqtt
        import time

        # backend setup
        client = mqtt.Client()
        mqtt_helper = MQTTHelper(client)

        # mqtt client setup
        client.username_pw_set(USERNAME, PASSWORD)
        client.connect(HOST, PORT)
        client.loop_start()

        # sleep to allow network traffic
        time.sleep(1)

        # test that the client connect
        assert mqtt_helper.on_connect_last_client == client
        assert mqtt_helper.on_connect_last_rc == 0

        # cleanup
        client.loop_stop()
        client.disconnect()

    @staticmethod
    def test_NWK_3():
        """
        Tests subscribing to a topic on a MQTT server with paho-mqtt
        """

        # imports
        import paho.mqtt.client as mqtt
        import time

        # backend setup
        client = mqtt.Client()
        mqtt_helper = MQTTHelper(client)

        # mqtt client setup
        client.username_pw_set(USERNAME, PASSWORD)
        client.connect(HOST, PORT)
        client.subscribe(TOPIC, 0)
        client.loop_start()

        # sleep to allow network traffic
        time.sleep(1)

        # test that the client subscribed
        assert mqtt_helper.on_subscribe_last_client == client

        # cleanup
        client.loop_stop()
        client.unsubscribe(TOPIC)
        client.disconnect()

    # @staticmethod
    # def test_NWK_4():
    #     """
    #     Tests publishing to a topic on a MQTT server with paho-mqtt
    #     """
    #     assert 1 == 1

    # @staticmethod
    # def test_NWK_5():
    #     """
    #     Tests receiving a message from a MQTT server with paho-mqtt
    #     """
    #     assert 1 == 1

    # @staticmethod
    # def test_NWK_6():
    #     """
    #     Tests unsubscribing from a topic on a MQTT server with paho-mqtt
    #     """
    #     assert 1 == 1

    # @staticmethod
    # def test_NWK_7():
    #     """
    #     Tests leaving (disconnecting) from a MQTT server with paho-mqtt
    #     """
    #     assert 1 == 1

    def on_connect(self, client, user_data, flags, rc):
        self.on_connect_last_rc = rc
        print("connected with result code {}".format(rc))

    def on_message(self, client, user_data, msg):
        pass

if __name__ == '__main__':
    unittest.main()
