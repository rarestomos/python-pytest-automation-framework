"""
This module contains the fixtures defined to be shared among all tests in 'users' test suite.
"""

import pytest
import uuid

from actions.user_endpoint_actions import post_request_to_create_user, delete_request_for_user
from models.users_model import get_valid_create_user_payload


@pytest.fixture
def invalid_user_id():
    """
    Setup method that generates UUID that will be used as fake user_id in test functions
    :return: The user ID that does not exist
    """
    not_existing_user_id = str(uuid.uuid4())
    return not_existing_user_id


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
    delete_request_for_user(user_id=user_id)
