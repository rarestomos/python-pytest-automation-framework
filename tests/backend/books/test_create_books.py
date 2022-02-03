"""
This module covers the POST test cases for the /books endpoint
"""

import pytest
from assertpy import assert_that, soft_assertions

from actions.books_endpoint_actions import post_request_to_create_book
from models.books_model import get_valid_book_payload_minimum_required, get_add_book_payload_without_parameter


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.create_books
def test_book_can_be_created(create_valid_book):
    with soft_assertions():
        assert_that(create_valid_book[0].status_code) \
            .described_as('POST request to the /books endpoint did not respond with success!') \
            .is_equal_to(200)
        assert_that(create_valid_book[0].json()) \
            .described_as('Trying to create a new book did not revert the right message!') \
            .has_name(create_valid_book[1]['name']) \
            .has_author(create_valid_book[1]['author']) \
            .has_description(None) \
            .has_cover(None)


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.create_books
def test_book_can_be_created_with_all_params(create_book_all_details):
    with soft_assertions():
        assert_that(create_book_all_details[0].status_code) \
            .described_as('POST request to the /books endpoint did not respond with success!') \
            .is_equal_to(200)
        assert_that(create_book_all_details[0].json()) \
            .described_as('Trying to create a new book did not revert the right message!') \
            .is_equal_to(create_book_all_details[1], ignore="id")


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.create_books
@pytest.mark.parametrize('param', ['author', 'name'])
def test_create_book_existing_author_different_param(create_valid_book, param):
    same_entity = create_valid_book[1][param]
    request_body = get_valid_book_payload_minimum_required()
    request_body[param] = same_entity
    response = post_request_to_create_book(request_body)
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as('POST request to the /books endpoint did not respond with success!') \
            .is_equal_to(200)
        book = response.json()
        request = request_body
        assert_that(book) \
            .has_name(request['name']) \
            .has_author(request['author']) \
            .has_description(None) \
            .has_cover(None)


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.create_books
def test_cannot_add_several_books_with_same_name_author(create_valid_book):
    response = post_request_to_create_book(create_valid_book[1])
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as('Trying to POST a new book with the same name and author did not revert 400 status code!') \
            .is_equal_to(400)
        assert_that(response.json()) \
            .described_as('Trying to POST a new book with the same name and author did not revert the right message!') \
            .is_equal_to(f"Book with name: {create_valid_book[1]['name']} written by author:"
                         f" {create_valid_book[1]['author']} already exists")


@pytest.mark.backend
@pytest.mark.books
@pytest.mark.create_books
@pytest.mark.parametrize('param', ['name', 'author'])
def test_cannot_create_book_without_param(param):
    request_body = get_add_book_payload_without_parameter(param=param)
    response = post_request_to_create_book(request_body)
    with soft_assertions():
        assert_that(response.status_code) \
            .described_as(f'Trying to POST a new book without "{param}" did not revert 400 status code!') \
            .is_equal_to(400)
        assert_that(response.json()) \
            .described_as(f'Trying to POST a new book without "{param}" did not revert the right message!') \
            .is_equal_to(f"'{param}' is required")
