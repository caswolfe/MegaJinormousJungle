import configparser


def generate_config():
    """
    Generate's and saves a new config file
    :return:
    """
    config = configparser.ConfigParser()

    config['GENERAL'] = {}

    config['MQTT'] = {}
    config['MQTT']['host'] = 'postman.cloudmqtt.com'
    config['MQTT']['port'] = '13272'
    config['MQTT']['user'] = 'jumpy-user'
    config['MQTT']['pass'] = 'password'

    with open('../config.ini', 'w') as config_file:
        config.write(config_file)