import os
import shutil
import tempfile
import logging

from DataPacketSaveDump import DataPacketSaveDump


class Workspace:

    TEMP_DIR: str = "C:/jumpy_temp"

    def __init__(self):

        self.log = logging.getLogger('jumpy')

        # if the workspace is an active/valid workspace
        self.is_active: bool = False

        # the directory in which this workspace is acting
        self.directory: str = None

        # the files in the directory
        self.files: list[str] = list()

        # flag to signify when a new file is added
        self.new_file_added = False

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
        try:
            shutil.rmtree(self.TEMP_DIR)
        except Exception as e:
            self.log.warning(e)

    def use_temp_workspace(self):
        self.log.debug('workspace using temporary directory')
        try:
            shutil.rmtree(self.TEMP_DIR)
        except Exception as e:
            self.log.warning(e)
        try:
            os.mkdir(self.TEMP_DIR)
        except FileExistsError as fee:
            self.log.warning(fee)
        self.directory = self.TEMP_DIR
        self.is_active = True

    def apply_data_packet_save_dump(self, packet: DataPacketSaveDump):
        self.log.debug('Applying {}'.format(packet.data_dict.get('document')))
        document: str = packet.data_dict.get('document')
        text: str = packet.data_dict.get('text')

        try:
            self.log.debug('dir: \'{}\''.format(self.directory))
            self.log.debug('doc: \'{}\''.format(document))
            full_qualified_file_name = self.directory + '/' + document
            self.log.debug('attempting to save \'{}\' to \'{}\''.format(document, full_qualified_file_name))

            if not os.path.isfile(full_qualified_file_name):
                self.new_file_added = True

            temp = open(full_qualified_file_name, 'w+')
            temp.close()

            file = open(full_qualified_file_name, 'r+')
            file.seek(0)
            file.write(text)
            file.close()
            self.files.append(document)
            self.log.debug('Saved to \'{}\''.format(full_qualified_file_name))
        except EnvironmentError as ee:
            self.log.error(ee)

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
