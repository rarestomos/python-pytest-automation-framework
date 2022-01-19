"""
This module covers the WebDriver Interface for UI testing framework Test Cases.
"""

import sys
from tokenize import String

from pychromedriver import chromedriver_path
from pygeckodriver import geckodriver_path
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def get_driver(browser: String):
    this_module = sys.modules[__name__]
    if not hasattr(this_module, f'{browser}_driver'):
        # Get list of methods that end with "driver" except the current one, remove the trailing _driver to print them
        available_browsers = [i[:-len('_driver')] for i in dir(this_module) if
                              i.endswith('_driver') and not i == 'get_driver']
        raise Exception(f'Unsupported driver. Available values for browser: {available_browsers}')
    driver = getattr(this_module, f'{browser}_driver')()
    return driver


def chrome_driver():
    driver_path = chromedriver_path
    caps = DesiredCapabilities.CHROME
    caps['acceptSslCerts'] = True
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_experimental_option('useAutomationExtension', False)
    options.accept_untrusted_certs = True
    options.assume_untrusted_cert_issuer = True
    driver = webdriver.Chrome(chrome_options=options, desired_capabilities=caps, executable_path=driver_path)
    return driver


def headless_chrome_driver():
    driver_path = chromedriver_path
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options, executable_path=driver_path)
    return driver


def firefox_driver():
    caps = DesiredCapabilities.FIREFOX
    caps['marionette'] = True
    caps['acceptSslCerts'] = True
    profile = webdriver.FirefoxProfile()
    profile.set_preference('app.update.auto', False)
    profile.set_preference('app.update.enabled', False)
    return webdriver.Firefox(profile, capabilities=caps, executable_path=geckodriver_path)
