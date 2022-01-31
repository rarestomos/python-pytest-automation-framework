"""
This module covers the DELETE test cases for the /users endpoint
"""

import pytest
from assertpy import soft_assertions, assert_that

from actions.users_endpoint_actions import delete_request_for_user


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.delete_users
def test_user_can_be_deleted(create_valid_user):
    user_id = create_valid_user[0].json()['id']
    delete_response = delete_request_for_user(user_id)
    with soft_assertions():
        assert_that(delete_response.status_code) \
            .described_as('DELETE request to the /users endpoint did not respond with success!') \
            .is_equal_to(200)
        assert_that(delete_response.json()) \
            .described_as('DELETE request to the /users endpoint did not revert the right message!') \
            .is_equal_to(f'Successfully deleted user {user_id}')


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.delete_users
def test_cannot_delete_user_with_invalid_user_id(invalid_id):
    delete_response = delete_request_for_user(invalid_id)
    with soft_assertions():
        assert_that(delete_response.status_code) \
            .described_as('Trying to DELETE user with user id that does not exist did not revert 400 status code!') \
            .is_equal_to(400)
        assert_that(delete_response.json()) \
            .described_as('Trying to DELETE user with user id that does not exist did not revert the right message!') \
            .is_equal_to(f'User with id = {invalid_id} was not found')
