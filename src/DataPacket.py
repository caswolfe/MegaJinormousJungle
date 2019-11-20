import uuid
import json
from datetime import datetime


class DataPacket:

    def __init__(self):
        self.data_dict = dict()
        self.data_dict.update({'packet-name': type(self).__name__})
        self.data_dict.update({'mac-addr': hex(uuid.getnode())})
        self.data_dict.update({'time-of-creation': str(datetime.now())})

    def set_time_of_send(self) -> None:
        """
        sets the time-of-send to the current system time, meant ot be called right before sending
        """
        self.data_dict.update({'time-of-send': str(datetime.now())})

    def update_data_dict(self) -> None:
        """
        Updates the data_dict to hold the current values of the variables
        """
        pass

    def parse_json(self, json_str: str) -> None:
        """
        Parses the provided JSON setting all parameters of the packet to those specified in the given JSON

        :param json_str: The JSON to be parsed
        """
        to_load: dict = json.loads(json_str)
        if to_load.get('packet-name') != type(self).__name__:
            raise Exception("provided JSON is not that of a DataPacket")
        else:
            self.data_dict = json.loads(json_str)

    def get_json(self) -> str:
        """
        updates the data_dict with the current Packet variables and converts to JSON

        :return: a JSON str with all of the data_dict variables
        """
        self.update_data_dict()
        return json.dumps(self.data_dict)

    def __eq__(self, other) -> bool:
        if not isinstance(self, object):
            return False

        return self.data_dict == other.data_dict
