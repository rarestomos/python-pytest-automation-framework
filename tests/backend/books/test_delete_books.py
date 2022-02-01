"""
This module covers the DELETE test cases for the /books endpoint
"""

import pytest
from assertpy import soft_assertions, assert_that

from actions.books_endpoint_actions import delete_request_for_book


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.delete_books
def test_book_can_be_deleted(create_valid_book):
    book_id = create_valid_book[0].json()['id']
    delete_response = delete_request_for_book(book_id)
    with soft_assertions():
        assert_that(delete_response.status_code) \
            .described_as('DELETE request to the /books endpoint did not respond with success!') \
            .is_equal_to(200)
        assert_that(delete_response.json()) \
            .described_as('DELETE request to the /books endpoint did not revert the right message!') \
            .is_equal_to(f'Successfully deleted book {book_id}')


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.delete_books
def test_cannot_delete_book_with_invalid_book_id(invalid_id):
    delete_response = delete_request_for_book(invalid_id)
    with soft_assertions():
        assert_that(delete_response.status_code) \
            .described_as('Trying to DELETE book with book_id that does not exist did not revert 400 status code!') \
            .is_equal_to(400)
        assert_that(delete_response.json()) \
            .described_as('Trying to DELETE book with book_id that does not exist did not revert the right message!') \
            .is_equal_to(f'Book with id = {invalid_id} was not found')
