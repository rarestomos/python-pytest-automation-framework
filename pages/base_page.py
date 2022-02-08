"""
This module contains the reference of the elements of the Base Page.
"""

from abc import ABC

from configuration.configuration import max_timeout, frontend_url


class BasePage(ABC):
    url = frontend_url
    create_button_locator = "#create"
    search_field_locator = "#searchField"
    row_selector = ".clickable-row[data-id='{0}']"

    def __init__(self, se):
        self.se = se
        self.max_timeout = max_timeout

    def filter_table(self, search_term):
        self.se.find(self.search_field_locator, wait=True, ttl=self.max_timeout).write(search_term)
        return self

    def select_table_row(self, data_id):
        self.se.find(self.row_selector.format(data_id), wait=True, ttl=self.max_timeout).click()
