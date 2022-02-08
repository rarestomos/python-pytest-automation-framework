"""
This module covers the UI interface TCs for Books pages.
"""

import pytest
from assertpy import assert_that, soft_assertions

from models.books_model import get_valid_book_payload_minimum_required
from pages.books.books_page import BooksPage
from pages.books.create_book_page import CreateBookPage


@pytest.mark.ui
@pytest.mark.books
def test_get_all_books_ui(create_book_all_details, se_element):
    se_element.navigate(BooksPage.url)
    books_page = BooksPage(se_element)
    assert_that(books_page.check_books_displayed()) \
        .described_as('I cannot see a list of available books in UI!') \
        .is_true()


@pytest.mark.ui
@pytest.mark.books
def test_book_can_be_added_ui(se_element):
    book = get_valid_book_payload_minimum_required()
    books_page = BooksPage(se_element)
    se_element.navigate(books_page.url)
    create_book_page = books_page.open_create_book(CreateBookPage)
    books_page = create_book_page.fill_in_book_details(book).click_create_book_button(BooksPage)
    with soft_assertions():
        assert_that(books_page.is_success_message_displayed(book.get("name"))) \
            .described_as('An error occurred while trying to create a book from UI!') \
            .is_true()
        assert_that(books_page.is_book_present_on_page(book)) \
            .described_as('Could not be able to locate newly created book into current books list!') \
            .is_true()


@pytest.mark.ui
@pytest.mark.books
def test_filter_books(create_book_all_details, se_element):
    se_element.navigate(BooksPage.url)
    books_page = BooksPage(se_element)
    search_term = "Angel"
    books_page.filter_table(search_term)
    assert_that(books_page.is_text_present_in_all_rows(search_term)) \
        .described_as('Could not perform search in Books UI page!') \
        .is_true()


@pytest.mark.ui
@pytest.mark.books
def test_view_book_details(create_book_all_details, se_element):
    se_element.navigate(BooksPage.url)
    books_page = BooksPage(se_element)
    book_id = create_book_all_details[0].json()['id']
    details_modal = books_page.open_book_details(book_id)
    with soft_assertions():
        book = create_book_all_details[0].json()
        book_details_modal = details_modal
        assert_that(book_details_modal.check_modal_is_displayed()) \
            .described_as('The View Book Details Modal could not be reached!') \
            .is_true()
        assert_that(book_details_modal.check_modal_title()) \
            .described_as('The View Book Details Modal has an unexpected title!') \
            .is_true()
        assert_that(book_details_modal.check_book_details(book)) \
            .described_as('The Book Details Modal contains incorrect information!') \
            .is_true()
