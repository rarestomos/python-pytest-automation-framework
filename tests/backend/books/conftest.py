"""
This module contains the fixtures defined to be shared among all tests in 'books' test suite.
"""

import pytest

from actions.books_endpoint_actions import post_request_to_create_book, delete_request_for_book
from models.books_model import get_valid_book_payload_minimum_required, get_valid_book_payload_all_params
from tests import logger


@pytest.fixture
def create_valid_book():
    """
    Setup and Teardown method for test functions that required new book to be created.
    Setup: book creation
    Teardown: book removal
    :return: The response object after POST request for book creation and the request payload used for it.
    """
    request_body = get_valid_book_payload_minimum_required()
    response = post_request_to_create_book(request_body)
    yield response, request_body
    book_id = response.json()['id']
    delete_response = delete_request_for_book(book_id=book_id)
    logger.debug(f'Got response: {delete_response.json()}' if response.ok
                 else f'Status code was {delete_response.status_code} because {delete_response.reason}')


@pytest.fixture
def create_book_all_details():
    """
    Setup and Teardown method for test functions that required new book to be created.
    Setup: book creation with all possible details
    Teardown: book removal
    :return: The response object after POST request for book creation and the request payload used for it.
    """
    request_body = get_valid_book_payload_all_params()
    response = post_request_to_create_book(request_body)
    yield response, request_body
    book_id = response.json()['id']
    delete_response = delete_request_for_book(book_id=book_id)
    logger.debug(f'Got response: {delete_response.json()}' if response.ok
                 else f'Status code was {delete_response.status_code} because {delete_response.reason}')
