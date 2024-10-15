import time
from selenium.webdriver.common.keys import Keys
from util.common import Page
from pageobject.login_pages_object import LoginPagesObject


class LoginPage(Page):

    def enter_login_credentials_gmail(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        time.sleep(3)

    def click_sign_in(self):
        self.wait_for_clickable(LoginPagesObject.SIGN_IN_BTN)
        self.wait_for(LoginPagesObject.SIGN_IN_BTN).click()

    def enter_username(self, username):
        self.wait_for_clickable(LoginPagesObject.USERNAME_INPUT)
        self.enter_input(LoginPagesObject.USERNAME_INPUT, username)
        self.find(LoginPagesObject.USERNAME_INPUT).send_keys(Keys.ENTER)

    def enter_password(self, password):
        self.wait_for_clickable(LoginPagesObject.PASSWORD_INPUT)
        self.enter_input(LoginPagesObject.PASSWORD_INPUT, password)
        self.find(LoginPagesObject.PASSWORD_INPUT).send_keys(Keys.ENTER)
