import os
import tempfile
import logging

from DataPacketSaveDump import DataPacketSaveDump


class Workspace:

    def __init__(self):

        self.log = logging.getLogger('jumpy')

        # if the workspace is an active/valid workspace
        self.is_active: bool = False

        # the directory in which this workspace is acting
        self.directory: str = None

        # the files in the directory
        self.files: list[str] = list()

    def open_directory(self, directory: str):
        self.directory = directory
        folder = os.listdir(self.directory)
        self.files.clear()
        for item in folder:
            if os.path.isfile(self.directory + "/" + item) and not item.startswith("."):
                self.log.debug('found \'{}\' in workspace'.format(item))
                self.files.append(item)
        self.is_active = True

    def close_workspace(self):
        self.is_active = False

    def create_temp_workspace(self):
        self.directory = tempfile.TemporaryDirectory()
        self.is_active = True

    def apply_data_packet_save_dump(self, packet: DataPacketSaveDump):
        document: str = packet.data_dict.get('document')
        text: str = packet.data_dict.get('text')

        file = open(self.directory + '/' + document, 'w')
        file.write(text)
        file.close()

    def get_save_dump(self) -> list():
        packets = list()
        for item in self.files:
            packet = DataPacketSaveDump()
            file = open(self.directory + '/' + item, 'r')
            text = file.read()
            file.close()
            packet.define_manually(item, text)
            packets.append(packet)
        return packets
