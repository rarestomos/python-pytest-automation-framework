"""
This module covers the Read Configuration File for DEV environment.
"""

import configparser
import os.path


class DevConfiguration:
    def __init__(self):
        self.configuration = configparser.ConfigParser(allow_no_value=True)
        path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        file_dir = os.path.join(path, 'dev_configuration.ini')
        with open(file=file_dir) as conf_file:
            self.configuration.read_file(f=conf_file, source='dev_configuration.ini')

    def read_configuration(self):
        pass
