import configparser
import json

import paho.mqtt.client as mqtt
import logging

import DataPacket


class NetworkHandler:
    """
    This class serves as a Socket wrapper for easy socket manipulation of the program.
    """

    TOPIC = 'jumpy-coms'

    is_connected = False

    def __init__(self, parse_message_function):

        # config setup
        self.config = configparser.ConfigParser()
        self.config.read('../config.ini')

        # MQTT client setup
        self.mc = mqtt.Client()
        self.mc.on_connect = self.mqtt_on_connect
        self.mc.on_message = self.mqtt_on_message
        self.mc.on_subscribe = self.mqtt_on_subscribe
        self.mc.on_publish = self.mqtt_on_publish
        self.mc.username_pw_set(self.config['MQTT']['user'], self.config['MQTT']['pass'])

        # logging setup
        self.log = logging.getLogger('jumpy')

        # network action handler setup
        self.parse_message_function = parse_message_function

        # used for unit testing
        self.unit_testing = False
        self.unit_testing_received_packet = None

        self.lobby = None
        # misc
        # self.mac = hex(uuid.getnode())

    def establish_connection(self) -> bool:
        """
        Establishes a connection to a peer.
        """

        self.log.debug('establishing a connection...')
        self.mc.connect(self.config['MQTT']['host'], int(self.config['MQTT']['port']))
        self.mc.subscribe(self.TOPIC, 0)
        self.mc.loop_start()
        self.is_connected = True

    def close_connection(self) -> None:
        """
        Closes the connection with a peer.
        """

        self.is_connected = False
        self.log.debug('disconnecting')
        self.mc.unsubscribe(self.TOPIC)
        self.mc.loop_stop()
        self.mc.disconnect()

    def join_lobby(self, lobby_name: str):
        self.lobby = lobby_name

    def close_lobby(self):
        self.lobby = None
        self.close_connection()

    def send_packet(self, packet: DataPacket) -> bool:
        """
        Broadcasts the specified packet to all peers.
        """
        if isinstance(packet, DataPacket.DataPacket):
            packet.set_time_of_send()
            self.log.debug('sending: {}'.format(packet.data_dict.get('packet-name')))
            # self.log.debug('sending: {}'.format(packet.get_json()))
            self.mc.publish(self.TOPIC, packet.get_json())
        else:
            self.mc.publish(self.TOPIC, packet)

    def mqtt_on_connect(self, client, userdata, rc):
        self.log.info('connected')

    def mqtt_on_message(self, client, userdata, msg):
        self.parse_message_function(msg.payload)

    def mqtt_on_subscribe(self, client, obj, mid, granted_qos):
        self.log.info('subscribed, qos \'{}\''.format(granted_qos[0]))

    def mqtt_on_publish(self):
        self.log.info('published')
