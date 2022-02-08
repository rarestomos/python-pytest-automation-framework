"""
This module contains the fixtures defined to be shared among all UI tests.
"""

import pytest
from elementium.drivers.se import SeElements

from configuration import BROWSER
from helpers.webdriver import get_driver


@pytest.fixture
def se_element():
    """
    Setup and Teardown method for test functions that require new SE Element based on Selenium to be created.
    Setup: book creation
    Teardown: book removal
    :return: The response object after POST request for book creation and the request payload used for it.
    """
    driver = get_driver(browser=BROWSER)
    se = SeElements(driver)
    yield se
    driver.quit()
