"""
This module contains the actions related to /users endpoint.
"""

import json
import requests

from actions import logger
from configuration.configuration import users_url


#  GET
def get_request_for_all_users():
    """
    Do a GET request for all existing users
    :return: the full response object
    """
    url = users_url
    logger.debug(f'Doing a GET ALL request to the USERS endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because: {response.reason}')
    return response


def get_request_for_user(user_id):
    """
    Do a GET request for one user
    :param user_id: the ID of the user
    :return: the user details
    """
    url = f'{users_url}/{user_id}'
    logger.debug(f'Doing a GET one user request to the USERS endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because: {response.reason}')
    return response


#  POST
def post_request_to_create_user(user):
    """
    Do a POST request to add a user
    :param user: the new user details
    :return: the full response object
    """
    url = users_url
    logger.debug(f'Doing a POST request to the endpoint: {url}')
    response = requests.post(url=url, data=json.dumps(user))
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because: {response.reason}')
    return response


#  DELETE
def delete_request_for_user(user_id):
    """
    Do a DELETE request for one user
    :param user_id: the ID of the user
    :return: message after delete action
    """
    url = f'{users_url}/{user_id}'
    logger.debug(f'Doing a DELETE one user request to the USERS endpoint: {url}')
    response = requests.delete(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because: {response.reason}')
    return response
