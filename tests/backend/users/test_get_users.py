"""
This module covers the GET test cases for the /users endpoint
"""

import pytest
from assertpy import assert_that, soft_assertions

from actions.user_endpoint_actions import (get_request_for_all_users,
                                           post_request_to_create_user,
                                           get_request_for_user)
from models.users_model import get_valid_create_user_payload


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.get_users
def test_get_all_users():
    response = get_request_for_all_users()
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as('GET request to the /users endpoint did not respond with success!') \
            .is_equal_to(200)
        assert_that(response.json()) \
            .described_as('GET request to the /users endpoint is not a type of list!') \
            .is_type_of(list)
        assert_that(response.json()[0].keys()) \
            .described_as('GET request to the /users endpoint does not revert the right keys in one list item!') \
            .contains_only('id', 'first_name', 'last_name', 'email')


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.get_users
def test_users_list_incremented_after_new_user_added():
    all_users_response = get_request_for_all_users()
    number_of_users_before = len(all_users_response.json())
    valid_request_body = get_valid_create_user_payload()
    post_request_to_create_user(valid_request_body)
    all_users_response = get_request_for_all_users()
    number_of_users_after = len(all_users_response.json())
    assert_that(number_of_users_after) \
        .described_as('The list of users was not incremented after creating a new user!') \
        .is_equal_to(number_of_users_before + 1)


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.get_users
def test_get_valid_user_details(create_valid_user):
    valid_user_id = create_valid_user[0].json()['id']
    get_response = get_request_for_user(user_id=valid_user_id)
    user = get_response.json()
    with soft_assertions():
        assert_that(get_response.status_code) \
            .described_as('The newly created user could not be successfully retrieved!') \
            .is_equal_to(200)
        assert_that(user) \
            .described_as('The newly created user is not properly displayed on GET one user request!') \
            .has_id(valid_user_id) \
            .has_first_name(create_valid_user[1]['first_name']) \
            .has_last_name(create_valid_user[1]['last_name']) \
            .has_email(create_valid_user[1]['email'])


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.get_users
def test_get_invalid_user_details(invalid_user_id):
    get_response = get_request_for_user(user_id=invalid_user_id)
    with soft_assertions():
        assert_that(get_response.status_code) \
            .described_as('Trying to GET a not existing user did not revert 400 status code!') \
            .is_equal_to(400)
        assert_that(get_response.json()) \
            .described_as('Trying to GET a not existing user did not revert the right message!') \
            .is_equal_to(f'User with id = {invalid_user_id} was not found')
