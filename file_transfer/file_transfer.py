# author: Rohan Joshi

import os
import sys
import logging
import yaml
import datetime
import tarfile
from fabric.api import execute, put
from fabric.network import disconnect_all

logging.basicConfig(filename="file_transfer.log", level=logging.DEBUG, format='%(asctime)s %(funcName)5s() %(levelname)s:  %(message)s', datefmt='%I:%M:%S %p')


class File_Transfer:

    def __init__(self):
        logging.debug("Initializing File_Transfer")
        self.setup_logging_file()
        self.get_values()
        self.hostname = self.values_dict['hostname']
        self.source_dir = self.values_dict['source_dir']
        self.remote_dir = self.values_dict['remote_dir']

    def get_values(self):
        logging.debug("checking presence of values file")
        if os.path.exists("/home/rohan/Documents/Programs/sideprojects/side_programs/file_transfer_values.yaml"):
            logging.debug("file present, checking")
            print("file present, checking")
        else:
            logging.error("cannot find file_transfer_values.yaml file, exiting")
            print("ERROR: cannot find file_transfer_values.yaml file, exiting")
            sys.exit(1)

        self.values_dict = yaml.load(open("file_transfer_values.yaml"))
        for key, value in self.values_dict.items():
            print(key + " is " + str(value))
            self.validate_current_value(key, value)


    def validate_current_value(self, key, value):
        logging.debug("checking " + str(key) + " in file_transfer_values.yaml")
        if value == " " or value == "default":
            logging.error(key + " is not valid, exiting")
            print("ERROR: " + str(key) + " is not valid, exiting")
            sys.exit(1)

    def setup_logging_file(self):
        open("file_transfer.log", "w").close()
        logging.debug("Cleared log file for this run")

    def get_server(self):
        logging.debug("Getting remote server connection")
        self.ping_test()
        logging.debug("Ping test successful, continue")
        self.get_source_files()

    def ping_test(self):
        response = os.system("ping -c 1 " + self.hostname)
        print("performing ping test")
        logging.debug("checking ping response")

        if response == 0:
            logging.debug("Can reach the server through the ping test, connection is good")
            print("ping test successful")
        else:
            print("ping test unsuccessful")
            logging.error("Cannot reach the server through the ping test, connection is not good.")
            logging.error("Check the hostname/IP address of the remote server, and verify if it can be reached")
            sys.exit(1)

    def get_source_files(self):
        logging.debug("Getting source files from " + self.source_dir)
        if os.path.isdir(self.source_dir):
            print("checking directory")
            logging.debug("found directory, listing files in directory")
            no_of_files = self.check_dir_contents()
            if no_of_files == 0:
                logging.error("No files, exiting")
                print("ERROR: The source directory does not contain any files to transfer, exiting")
            else:
                logging.debug("Retrieved number of files, will now transfer")
                self.backup_files()
        else:
            print("ERROR: Could not find directory, exiting")
            logging.error("Could not find directory, exiting")

    def check_dir_contents(self):
        logging.debug("checking files in directory")
        path, dirs, files = os.walk(self.source_dir).next()
        file_count = len(files)
        logging.debug("the source directory contains number of files: " + str(file_count))

        if file_count <= 0:
            logging.error("The source directory contains no files, exiting")
            return 0
        else:
            return 1

    def backup_files(self):
        logging.debug("backing up files to remote server")
        currentDT = datetime.datetime.now()
        self.tar_file_name = "backup-" + currentDT.strftime("%Y-%m-%d") + ".tar.gz"

        logging.debug("archiving current files to move to server")
        print("compressing current tree")
        with tarfile.open(self.tar_file_name,"w:gz") as tar:
            tar.add(self.source_dir, arcname=os.path.basename(self.source_dir))
        file_to_send = self.tar_file_name
        print("begin copy of files to backup server")
        try:
            s = execute(put, file_to_send, self.remote_dir, host=self.hostname)
            print(repr(s))
        finally:
            disconnect_all()

        logging.debug("complete...")
        self.cleanup()

    def cleanup(self):
        logging.debug("removing generated tar file")
        print("removing generated tar file")
        os.system("rm " + self.tar_file_name)


ft = File_Transfer()
ft.get_server()
