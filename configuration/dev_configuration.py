"""
This module covers the Read Configuration File for DEV environment.
"""

import os.path

import configparser

from configuration import ENV_NAME


class DevConfiguration:
    def __init__(self):
        self.configuration = configparser.ConfigParser(allow_no_value=True)
        path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        file_dir = os.path.join(path, 'dev_configuration.ini')
        with open(file=file_dir) as conf_file:
            self.configuration.read_file(f=conf_file, source='dev_configuration.ini')

    def read_configuration(self):
        self.backend_url = self.configuration[ENV_NAME]['backend_url']
        self.frontend_url = self.configuration[ENV_NAME]['frontend_url']
        self.users_url = f'{self.backend_url}/users'
        self.books_url = f'{self.backend_url}/books'
        self.max_timeout = int(self.configuration[ENV_NAME]["max_timeout"])
