"""
This module covers the GET test cases for the /books endpoint
"""

import pytest
from assertpy import soft_assertions, assert_that

from actions.books_endpoint_actions import (get_request_for_all_books,
                                            post_request_to_create_book,
                                            delete_request_for_book,
                                            get_request_for_book)
from models.books_model import get_valid_book_payload_minimum_required


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.get_books
def test_get_all_books(create_valid_book):
    all_books_response = get_request_for_all_books()
    with soft_assertions():
        assert_that(all_books_response.status_code) \
            .described_as('GET request to the /books endpoint did not respond with success!') \
            .is_equal_to(200)
        assert_that(all_books_response.json()[0]) \
            .described_as('GET request to the /users endpoint does not revert the right keys in one list item!') \
            .contains_only('id', 'name', 'author', 'description', 'cover')


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.get_books
def test_books_list_incremented_after_new_book_added():
    all_books_response = get_request_for_all_books()
    number_of_books_before = len(all_books_response.json())
    valid_request_body = get_valid_book_payload_minimum_required()
    response = post_request_to_create_book(valid_request_body)
    all_books_response = get_request_for_all_books()
    number_of_books_after = len(all_books_response.json())
    assert_that(number_of_books_after) \
        .described_as('The list of books was not incremented after creating a new user!') \
        .is_equal_to(number_of_books_before + 1)
    book_id = response.json()['id']
    delete_request_for_book(book_id=book_id)


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.get_books
def test_get_book_details_added_with_required_parameters_only(create_valid_book):
    valid_book_id = create_valid_book[0].json()['id']
    response = get_request_for_book(book_id=valid_book_id)
    book = response.json()
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as('The newly created book could not be successfully retrieved!') \
            .is_equal_to(200)
        assert_that(book['id']) \
            .described_as('The newly created book has a different ID on GET than the one seen on creation/POST!') \
            .is_equal_to(valid_book_id)
        assert_that(book) \
            .described_as('The newly created book is not properly displayed on GET one book request!') \
            .is_equal_to(create_valid_book[1], ignore=['id', 'description', 'cover'])


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.get_books
def test_get_book_details_added_with_all_params(create_book_all_details):
    valid_book_id = create_book_all_details[0].json()['id']
    response = get_request_for_book(book_id=valid_book_id)
    book = response.json()
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as('The newly created book could not be successfully retrieved!') \
            .is_equal_to(200)
        assert_that(book['id']) \
            .described_as('The newly created book has a different ID on GET than the one seen on creation/POST!') \
            .is_equal_to(valid_book_id)
        assert_that(book) \
            .described_as('The newly created book is not properly displayed on GET one book request!') \
            .is_equal_to(create_book_all_details[1], ignore=['id', 'description', 'cover'])


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.get_books
def test_get_invalid_book_details(invalid_id):
    get_response = get_request_for_book(book_id=invalid_id)
    with soft_assertions():
        assert_that(get_response.status_code) \
            .described_as('Trying to GET a not existing book did not revert 400 status code!') \
            .is_equal_to(400)
        assert_that(get_response.json()) \
            .described_as('Trying to GET a not existing book did not revert the right message!') \
            .is_equal_to(f'Book with id = {invalid_id} was not found')
