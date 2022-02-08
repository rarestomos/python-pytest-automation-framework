"""
This module contains the reference of the elements (page object) of the Book Details Modal.
"""

from configuration.configuration import max_timeout


class BookDetailsModal:
    modal_locator = "#viewBookDetails"
    title_locator = "#itemLabel"
    title = "Book Details"
    cover_locator = "#preview"
    book_name_locator = "#book_name"
    author_name_locator = "#book_author"
    book_description_locator = "#book_description"

    def __init__(self, se):
        self.se = se
        self.max_timeout = max_timeout

    def check_modal_is_displayed(self):
        return self.se.find(self.modal_locator, wait=True, ttl=self.max_timeout).is_displayed()

    def check_modal_title(self):
        return self.se.find(self.title_locator, wait=True, ttl=self.max_timeout).text() == self.title

    def check_book_details(self, book):
        return (self.se.find(self.cover_locator, wait=True, ttl=self.max_timeout).attribute("src") == book["cover"]
                and self.se.find(self.book_name_locator, wait=True, ttl=self.max_timeout).text() == book["name"]
                and self.se.find(self.author_name_locator, wait=True, ttl=self.max_timeout).text() == book["author"]
                and self.se.find(self.book_description_locator, wait=True,
                                 ttl=self.max_timeout).text() == book["description"])
