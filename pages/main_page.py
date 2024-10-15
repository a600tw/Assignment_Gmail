import time
from selenium.webdriver.common.keys import Keys
from util.common import Page
from pageobject.main_pages_object import GmailPagesObject
from config import config


class GmailPage(Page):
    
    def send_email(self):
        self.wait_for_clickable(GmailPagesObject.COMPOSE_BTN)
        self.wait_for(GmailPagesObject.COMPOSE_BTN).click()

        self.wait_for_clickable(GmailPagesObject.INPUT_TO)
        self.find(GmailPagesObject.INPUT_TO).send_keys(config.SEND_TO)
        self.find(GmailPagesObject.INPUT_SUBJECT).send_keys(config.SUBJECT)
        self.find(GmailPagesObject.INPUT_BODY).send_keys(config.MAILBODY)

        self.wait_for_clickable(GmailPagesObject.OPTION_BTN)
        self.wait_for(GmailPagesObject.OPTION_BTN).click()

        self.wait_for_clickable(GmailPagesObject.LABEL_SELECTOR)
        self.wait_for(GmailPagesObject.LABEL_SELECTOR).click()

        self.wait_for_clickable(GmailPagesObject.SOCIAL_SELECTOR)
        self.wait_for(GmailPagesObject.SOCIAL_SELECTOR).click()

        self.wait_for_clickable(GmailPagesObject.SOCIAL_APPLY)
        self.wait_for(GmailPagesObject.SOCIAL_APPLY).click()

        self.wait_for_clickable(GmailPagesObject.SEND_BTN)
        self.wait_for(GmailPagesObject.SEND_BTN).click()

        time.sleep(5)

    def get_mail_form_social(self):
        self.wait_for(GmailPagesObject.SEARCH_MAIL_BAR)
        self.find(GmailPagesObject.SEARCH_MAIL_BAR).send_keys("category:social")
        self.find(GmailPagesObject.SEARCH_MAIL_BAR).send_keys(Keys.ENTER)
        self.starred_mail()
        self.get_first_mail()

    def starred_mail(self):
        self.refresh_page()
        self.wait_for_clickable(GmailPagesObject.STAR_MAIL)
        self.wait_for(GmailPagesObject.STAR_MAIL).click()
        time.sleep(5)

    def get_first_mail(self):
        self.refresh_page()
        self.wait_for(GmailPagesObject.FIRST_MAIL)
        mail = self.find_elements(GmailPagesObject.FIRST_MAIL)
        try:
            mail[0].click()
        except:
            mail[1].click()

    def get_mail_subject(self):
        subject = self.wait_for(GmailPagesObject.MAIL_SUBJECT)
        return subject.text

    def get_mail_body(self):
        body = self.wait_for(GmailPagesObject.MAIL_BODY)
        return body.text
    
    def get_mail_social_checked(self):
        self.wait_for_clickable(GmailPagesObject.OPTION_BTN_INMAIL)
        self.wait_for(GmailPagesObject.OPTION_BTN_INMAIL).click()
        self.wait_for_clickable(GmailPagesObject.LABEL_SELECTOR)
        self.wait_for(GmailPagesObject.LABEL_SELECTOR).click()
        social_status = self.wait_for(GmailPagesObject.SOCIAL_STATUS)
        return social_status.text


    def delete_mail(self):
        self.wait_for_clickable(GmailPagesObject.DELETE_MAIL)
        self.wait_for(GmailPagesObject.DELETE_MAIL).click()
        # time.sleep(2)
        self.refresh_page()
