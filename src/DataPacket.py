import uuid
import json
from datetime import datetime


class DataPacket:

    def __init__(self):
        self.data_dict = dict()
        self.data_dict.update({'packet-name': type(self).__name__})
        self.data_dict.update({'mac-addr': hex(uuid.getnode())})
        self.data_dict.update({'time-of-creation': str(datetime.now())})

    def set_time_of_send(self):
        self.data_dict.update({'time-of-send': str(datetime.now())})

    def get_json(self):
        return json.dumps(self.data_dict)
