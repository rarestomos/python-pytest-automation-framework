"""
This module contains the fixtures defined to be shared among all tests in 'users' test suite.
"""

import pytest

from actions.users_endpoint_actions import post_request_to_create_user, delete_request_for_user
from models.users_model import get_valid_create_user_payload
from tests import logger


@pytest.fixture
def create_valid_user():
    """
    Setup and Teardown method for test functions that required new user to be created.
    Setup: user creation
    Teardown: user removal
    :return: The response object after POST request for user creation and the request payload used for it.
    """
    valid_request_body = get_valid_create_user_payload()
    response = post_request_to_create_user(valid_request_body)
    yield response, valid_request_body
    user_id = response.json()['id']
    delete_response = delete_request_for_user(user_id=user_id)
    logger.debug(f'Got response: {delete_response.json()}' if response.ok
                 else f'Status code was {delete_response.status_code} because {delete_response.reason}')
