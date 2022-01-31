"""
This module covers the PUT test cases for the /users endpoint
"""

import pytest
from assertpy import assert_that, soft_assertions

from actions.users_endpoint_actions import put_request_to_update_user
from tests import fake


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.edit_users
def test_user_details_can_be_edited(create_valid_user):
    new_first_name = fake.first_name()
    new_last_name = fake.last_name()
    create_valid_user[1]['first_name'] = new_first_name
    create_valid_user[1]['last_name'] = new_last_name
    user_id = create_valid_user[0].json()['id']
    response = put_request_to_update_user(user_id=user_id, user=create_valid_user[1])
    user = response.json()
    request = create_valid_user[1]
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as('PUT request to the /users endpoint did not respond with success!') \
            .is_equal_to(200)
        assert_that(user) \
            .described_as('Trying to edit an existing user did not revert the right message!') \
            .has_id(user_id) \
            .has_first_name(request['first_name']) \
            .has_last_name(request['last_name']) \
            .has_email(request['email'])


@pytest.mark.backend
@pytest.mark.users
@pytest.mark.edit_users
def test_user_email_cannot_be_edited(create_valid_user):
    create_valid_user[1]['email'] = fake.email()
    user_id = create_valid_user[0].json()['id']
    response = put_request_to_update_user(user_id=user_id, user=create_valid_user[1])
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as('Trying to update email for an existing user did not revert 400 status code!') \
            .is_equal_to(400)
        assert_that(response.json()) \
            .described_as('Trying to update email for an existing user did not revert the right message!') \
            .is_equal_to(f"'email' is invalid")
