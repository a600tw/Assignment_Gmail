from pages.login_page import LoginPage
from pages.main_page import GmailPage
from config import config

def test_gmail_functionality(gmail_driver):

    LoginPage(gmail_driver).click_sign_in()
    LoginPage(gmail_driver).enter_login_credentials_gmail(config.USER, config.PASSWORD)
    GmailPage(gmail_driver).send_email()

    # Check if mail is filtered by "category:social"
    GmailPage(gmail_driver).get_mail_form_social()

    subject = GmailPage(gmail_driver).get_mail_subject()
    body = GmailPage(gmail_driver).get_mail_body()
    social = GmailPage(gmail_driver).get_mail_social_checked()

    assert subject == 'PB Test Mail'  # Assertion for mail subject
    assert body == 'PB Test WOW'  # Assertion for mail body
    assert social == 'Social'  # Assertion for Social selected