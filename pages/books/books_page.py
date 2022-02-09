"""
This module contains the reference of the elements (page object) of the Books Page.
"""

from pages.base_page import BasePage
from pages.books.book_details_modal import BookDetailsModal


class BooksPage(BasePage):
    clickable_row_locator = '.clickable-row'
    save_success_message_locator = '.alert-success'
    view_details_button_locator = '#viewDetails'

    def __init__(self, se):
        super().__init__(se)
        self.url = super().url + '/books'
        self.se = se

    def check_books_displayed(self):
        books = self.se.find(self.clickable_row_locator, wait=True, ttl=self.max_timeout)
        return len(books) > 0

    def open_create_book(self, next_page):
        self.se.find(self.create_button_locator, wait=True, ttl=self.max_timeout).click()
        return next_page(self.se)

    def is_success_message_displayed(self, book_name):
        success_msg = self.se.find(self.save_success_message_locator, wait=True, ttl=self.max_timeout)
        check_message = f"Book '{book_name}' was successfully saved" in success_msg.text()
        return len(success_msg) == 1 and check_message

    def is_book_present_on_page(self, book):
        books = self.se.find(self.clickable_row_locator, wait=True, ttl=self.max_timeout)
        for row in books:
            row_text = row.text()
            if book.get('name') in row_text and book.get('author') in row_text:
                return True
        return False

    def is_text_present_in_all_rows(self, text):
        books = self.se.find(self.clickable_row_locator, wait=True, ttl=self.max_timeout)
        for row in books:
            if text not in row.text():
                return False
        return True

    def open_book_details(self, book_id):
        self.select_table_row(data_id=book_id)
        self.se.find(self.view_details_button_locator, wait=True, ttl=self.max_timeout).click()
        return BookDetailsModal(self.se)
