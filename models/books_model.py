"""
Define books MODELS used across testing framework, based on namedtuple library.
"""

from collections import namedtuple

from models import fake


def _setup_create_book():
    """
    Create payload to Add Book
    :return:
    {
    "name": "Unknown",
    "author": "Unknown",
    "description": "paragraph",
    "cover": "Link to cover picture"
    }
    """
    BookModel = namedtuple("BookModel", ["name", "author", "description", "cover"])
    return BookModel(name=fake.text(20),
                     author=fake.name(),
                     description=fake.paragraph(nb_sentences=6),
                     cover="https://thebookcoverdesigner.com/wp-content/uploads/2019/08/249.jpg")


def get_valid_book_payload_all_params():
    request_body = dict(_setup_create_book()._asdict())
    return request_body


def get_valid_book_payload_minimum_required():
    request_body = dict(_setup_create_book()._asdict())
    del request_body['description']
    del request_body['cover']
    return request_body


def get_add_book_payload_without_parameter(param):
    request_body = dict(_setup_create_book()._asdict())
    del request_body[param]
    return request_body
