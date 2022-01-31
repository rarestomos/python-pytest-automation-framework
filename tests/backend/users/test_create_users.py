"""
This module covers the POST test cases for the /users endpoint
"""

import pytest
from assertpy import assert_that, soft_assertions

from actions.users_endpoint_actions import post_request_to_create_user
from models.users_model import get_valid_create_user_payload, get_add_user_payload_without_parameter


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.create_users
def test_user_can_be_created(create_valid_user):
    with soft_assertions():
        assert_that(create_valid_user[0].status_code) \
            .described_as('POST request to the /users endpoint did not respond with success!') \
            .is_equal_to(200)
        assert_that(create_valid_user[0].json()) \
            .described_as('Trying to create a new user did not revert the right message!') \
            .is_equal_to(create_valid_user[1], ignore="id")


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.create_users
def test_several_users_cannot_be_added_with_same_email(create_valid_user):
    same_email = create_valid_user[1]['email']
    new_request_body = get_valid_create_user_payload()
    new_request_body['email'] = same_email
    response = post_request_to_create_user(new_request_body)
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as('Trying to POST a new user with existing email address did not revert 400 status code!') \
            .is_equal_to(400)
        assert_that(response.json()) \
            .described_as('Trying to POST a new user with existing email address did not revert the right message!') \
            .is_equal_to(f'User with email: {same_email} already exists')


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.create_users
@pytest.mark.parametrize('param, reason',
                         [('first_name', 'required'), ('last_name', 'required'), ('email', 'required')])
def test_cannot_add_user_without_param(param, reason):
    request_body = get_add_user_payload_without_parameter(param=param)
    response = post_request_to_create_user(request_body)
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as(f'Trying to POST a new user without "{param}" did not revert 400 status code!') \
            .is_equal_to(400)
        assert_that(response.json()) \
            .described_as(f'Trying to POST a new user without "{param}" did not revert the right message!') \
            .is_equal_to(f"'{param}' is {reason}")


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.create_users
def test_cannot_add_user_with_invalid_email_format():
    request_body = get_valid_create_user_payload()
    request_body['email'] = 'abc'
    response = post_request_to_create_user(request_body)
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as(f'Trying to POST a new user with invalid email format did not revert 400 status code!') \
            .is_equal_to(400)
        assert_that(response.json()) \
            .described_as(f'Trying to POST a new user with invalid email format did not revert the right message!') \
            .is_equal_to("'email' is invalid")
