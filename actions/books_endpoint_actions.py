"""
This module contains the actions related to /books endpoint.
"""

import json
import requests

from actions import logger
from configuration.configuration import books_url


#  GET
def get_request_for_all_books():
    """
    Do a GET request for all existing books
    :return: the full response object
    """
    url = books_url
    logger.debug(f'Doing a GET request to the endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


def get_request_for_book(book_id):
    """
    Do a GET request for one book
    :param book_id: the ID of the book
    :return: the book details
    """
    url = f'{books_url}/{book_id}'
    logger.debug(f'Doing a GET request to the endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


#  POST
def post_request_to_create_book(book):
    """
    Do a post request to create a book
    :param book: the details of the new book
    :return: the full response object
    """
    url = books_url
    logger.debug(f'Doing a POST request to the endpoint: {url}')
    response = requests.post(url=url, data=json.dumps(book))
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


#  DELETE
def delete_request_for_book(book_id):
    """
    Do a DELETE request for one book
    :param book_id: the ID of the book
    :return: the message after delete action
    """
    url = f'{books_url}/{book_id}'
    logger.debug(f'Doing a DELETE request to the endpoint: {url}')
    response = requests.delete(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response