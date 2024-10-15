import pytest
from selenium import webdriver

import undetected_chromedriver as uc
from pages.main_page import GmailPage
from config import config


def create_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-single-click-autofill")
    driver = uc.Chrome(options=chrome_options)
    return driver


@pytest.fixture()
def gmail_driver():
    gmailurl = config.GMAIL_URL
    gmail_driver = create_chrome_driver()
    gmail_driver.get(gmailurl)

    yield gmail_driver

    # Delete mail for data teardown
    GmailPage(gmail_driver).delete_mail()
    gmail_driver.close()
