"""
This module contains the reference of the elements (page object) for the Create Book Page.
"""

from pages.base_page import BasePage


class CreateBookPage(BasePage):
    name_field_locator = '#name'
    author_field_locator = '#author'
    description_field_locator = '#description'
    cover_field_locator = '#cover'
    create_button_locator = '#save'
    cancel_button_locator = '#back'

    def __init__(self, se):
        super().__init__(se)
        self.url = super().url + '/books/create'
        self.se = se

    def fill_in_book_details(self, book_details: dict):
        self.se.find(self.name_field_locator, wait=True, ttl=self.max_timeout).write(book_details.get('name'))
        self.se.find(self.author_field_locator, wait=True, ttl=self.max_timeout).write(book_details.get('author'))
        self.se.find(self.description_field_locator, wait=True, ttl=self.max_timeout) \
            .write(book_details.get('description', ''))
        self.se.find(self.cover_field_locator, wait=True, ttl=self.max_timeout).write(book_details.get('cover', ''))
        return self

    def click_create_book_button(self, next_page):
        self.se.find(self.create_button_locator, wait=True, ttl=self.max_timeout).click()
        return next_page(self.se)

    def click_cancel_button(self):
        self.se.find(self.cancel_button_locator, wait=True, ttl=self.max_timeout).click()
        return CreateBookPage(self.se)
