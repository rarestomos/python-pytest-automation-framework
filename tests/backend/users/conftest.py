"""
This module contains the fixtures defined to be shared among all tests in 'users' test suite.
"""

import pytest
import uuid

from actions.user_endpoint_actions import post_request_to_create_user
from models.users_model import get_valid_create_user_payload


@pytest.fixture
def invalid_user_id():
    not_existing_user_id = str(uuid.uuid4())
    return not_existing_user_id


@pytest.fixture
def create_valid_user():
    valid_request_body = get_valid_create_user_payload()
    response = post_request_to_create_user(valid_request_body)
    return response, valid_request_body
