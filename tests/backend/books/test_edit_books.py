"""
This module covers the PUT test cases for the /books endpoint
"""

import pytest
from assertpy import soft_assertions, assert_that

from actions.books_endpoint_actions import put_request_to_update_book
from tests import fake


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.edit_books
def test_book_details_can_be_changed(create_valid_book):
    new_title = fake.text(20)
    new_author = fake.name()
    create_valid_book[1]['name'] = new_title
    create_valid_book[1]['author'] = new_author
    book_id = create_valid_book[0].json()['id']
    response = put_request_to_update_book(book_id=book_id, book=create_valid_book[1])
    book = response.json()
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as('PUT request to the /books endpoint did not respond with success!') \
            .is_equal_to(200)
        assert_that(book) \
            .described_as('Trying to edit an existing book did not revert the right message!') \
            .has_name(create_valid_book[1]['name']) \
            .has_author(create_valid_book[1]['author']) \
            .has_description(None) \
            .has_cover(None)


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.edit_books
def test_edit_book_with_same_details(create_valid_book):
    book_id = create_valid_book[0].json()['id']
    response = put_request_to_update_book(book_id=book_id, book=create_valid_book[1])
    book = response.json()
    assert_that(response.status_code) \
        .described_as('PUT request to the /books endpoint with the same details again did not respond with success!') \
        .is_equal_to(200)
    assert_that(book) \
        .described_as('Trying to edit an existing book with the same details again did not revert the right message!') \
        .has_name(create_valid_book[1]['name']) \
        .has_author(create_valid_book[1]['author']) \
        .has_description(None) \
        .has_cover(None)
