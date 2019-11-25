import os
import shutil
import tempfile
import logging
import sys 

from pathlib import Path
from DataPacketDocumentEdit import DataPacketDocumentEdit
from DataPacketSaveDump import DataPacketSaveDump
from DataPacketSaveRequest import DataPacketSaveRequest


class Workspace:

    TEMP_DIR: str = str(os.path.join(Path.home(), "Downloads"))

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

        self.is_host = False

    def get_workspace_size(self):
        return len(self.files)

    def open_directory(self, directory: str):
        self.log.debug('Opening directory: \'{}\''.format(directory))
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
        self.open_directory(self.TEMP_DIR)

    def apply_data_packet_save_dump(self, packet: DataPacketSaveDump):
        self.log.debug('Applying save dump for \'{}\''.format(packet.data_dict.get('document')))
        document: str = packet.data_dict.get('document')
        text: str = packet.data_dict.get('text')

        try:
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
        except EnvironmentError as ee:
            self.log.error(ee)

    def apply_data_packet_document_edit(self, packet: DataPacketDocumentEdit):
        if packet.get_document() not in self.files:
            self.log.error('RECEIVED DataPacketDocumentEdit FOR A DOCUMENT NOT IN THE CURRENT WORKSPACE')
            return
        full_qualified_file_name = self.directory + '/' + packet.get_document()
        file = open(full_qualified_file_name, 'w')
        file.seek(0)
        file.write(packet.get_text())
        file.close()

    # def apply_data_packet_document_edit(self, data_dict: dict()) -> bool:
    #     document: str = data_dict.get('document')
    #     if document not in self.files:
    #         self.log.error('RECEIVED DataPacketDocumentEdit FOR A DOCUMENT NOT IN THE CURRENT WORKSPACE')
    #         return
    #     full_qualified_file_name = self.directory + '/' + document
    #     file = open(full_qualified_file_name, 'r')
    #     file_text = file.read()
    #     file.close()
    #     file_text_hash = DataPacketDocumentEdit.get_text_hash(file_text)
    #     if data_dict.get('old_text_hash') != file_text_hash:
    #         self.log.error('Hash Mismatch!')
    #         return False
    #     applied_text = DataPacketDocumentEdit.apply_packet_data_dict(
    #         data_dict.get('old_text_hash'),
    #         data_dict.get('action'),
    #         data_dict.get('position'),
    #         data_dict.get('character'),
    #         file_text_hash,
    #         file_text
    #     )
    #
    #     file = open(full_qualified_file_name, 'w')
    #     file.seek(0)
    #     file.write(applied_text)
    #     file.close()
    #     return True

    def get_save_dump(self) -> list():
        packets = list()
        for item in self.files:
            packet = DataPacketSaveDump()
            file = open(self.directory + '/' + item, 'r')
            text = file.read()
            file.close()
            packet.set_document(item)
            packet.set_text(text)
            packet.set_workspace_size(self.get_workspace_size())
            packets.append(packet)
        return packets

    def get_save_dump_from_document(self, document: str):
        if document not in self.files:
            self.log.error('document \'{}\' not in the workspace...'.format(document))
            return None
        full_qualified_file_name = self.directory + '/' + document
        to_ret = DataPacketSaveDump()
        file = open(full_qualified_file_name, 'r')
        doc_text = file.read()
        file.close()
        to_ret.define_manually(document, doc_text)