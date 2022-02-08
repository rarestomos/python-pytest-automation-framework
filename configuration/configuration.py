"""
This module covers the Configuration Interface for functional testing framework.
"""

import importlib
import os

from configuration import __init_logging


def get_configuration():
    env = os.environ.get('env', 'dev')
    supported_envs = ['dev', 'test']
    __init_logging()
    if env not in supported_envs:
        raise EnvironmentError("Unsupported environment: " + env)
    module = importlib.import_module(f'configuration.{env}_configuration')
    class_name = f'{env}Configuration'
    class_attr = None
    for attr in dir(module):
        if attr.lower() == class_name.lower():
            class_attr = attr
    if not class_attr:
        raise ValueError(f'configuration class not found for environment {env}')
    config = getattr(module, class_attr)()
    return config


configuration = get_configuration()
configuration.read_configuration()

backend_url = configuration.backend_url
frontend_url = configuration.frontend_url
users_url = configuration.users_url
books_url = configuration.books_url
max_timeout = configuration.max_timeout
