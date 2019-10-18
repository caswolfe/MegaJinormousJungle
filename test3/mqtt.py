import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("jumpy-coms")  # Subscribe to the topic “digitest/test1”, receive any messages published on it


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg


client = mqtt.Client()  # Create instance of client with client ID “digi_mqtt_test”
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message
client.username_pw_set('jumpy-user', 'password')
# client.connect("m2m.eclipse.org", 1883, 60)  # Connect to (broker, port, keepalive-time)
client.connect('postman.cloudmqtt.com', 13272)
client.loop_forever()  # Start networking daemon

# mosquitto_sub -h postman.cloudmqtt.com -p 13272 -u jumpy-user -P password -t jumpy-coms
# mosquitto_pub -h postman.cloudmqtt.com -p 13272 -u jumpy-user -P password -t jumpy-coms -m "test"
