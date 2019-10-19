import configparser
import paho.mqtt.client as mqtt
import logging
import pickle

from src.DataPacket import DataPacket


class NetworkHandler:
    """
    This class serves as a Socket wrapper for easy socket manipulation of the program.
    """

    TOPIC = 'jumpy-coms'

    def __init__(self):

        # config setup
        self.config = configparser.ConfigParser()
        self.config.read('../config.ini')

        # MQTT client setup
        self.mc = mqtt.Client()
        self.mc.on_connect = self.mqtt_on_connect
        self.mc.on_message = self.mqtt_on_connect
        self.mc.on_subscribe = self.mqtt_on_subscribe
        self.mc.on_publish = self.mqtt_on_publish
        self.mc.username_pw_set(self.config['MQTT']['user'], self.config['MQTT']['pass'])

        # logging setup
        self.log = logging.getLogger('jumpy')

    def establish_connection(self) -> bool:
        """
        Establishes a connection to a peer.
        """

        self.log.debug('establishing a connection...')
        self.mc.connect(self.config['MQTT']['host'], int(self.config['MQTT']['port']))
        self.mc.subscribe(self.TOPIC, 0)
        self.mc.loop_start()

    def close_connection(self) -> None:
        """
        Closes the connection with a peer.
        """

        self.log.debug('disconnecting')
        self.mc.unsubscribe(self.TOPIC)
        self.mc.loop_stop()
        self.mc.disconnect()

    def open_lobby(self, lobby_name: str):
        pass

    def close_lobby(self, lobby_name: str):
        pass

    # def open_as_host(self) -> bool:
    #     """
    #     Opens connections with this machine as host.
    #     """
    #     pass
    #
    # def close_as_host(self) -> None:
    #     """
    #     Closes all connections with this machine as host.
    #     :return:
    #     """
    #     pass

    def add_network_action_handler(self) -> bool:
        """
        Adds a NetworkActionHandler to this SocketHandler.
        """
        pass

    def remove_network_action_handler(self) -> bool:
        """
        Removes the specified NetworkActionHandler from this SocketHandler.
        """
        pass

    def send_packet(self, packet: DataPacket) -> bool:
        """
        Broadcasts the specified packet to all peers.
        """
        if isinstance(packet, DataPacket):
            data = pickle.dumps(packet)
            self.mc.publish(self.TOPIC, str(data))
        else:
            self.mc.publish(self.TOPIC, packet)

    def mqtt_on_connect(self, client, userdata, rc):
        self.log.info('connected')

    def mqtt_on_message(self, client, userdata, msg):
        self.log.info('recieved: \'{}\''.format(msg))

    def mqtt_on_subscribe(self, client, obj, mid, granted_qos):
        self.log.info('subscribed')

    def mqtt_on_publish(self):
        self.log.info('published')
