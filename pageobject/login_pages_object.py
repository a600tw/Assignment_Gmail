from selenium.webdriver.common.by import By

class LoginPagesObject():

    USERNAME_INPUT = (By.XPATH, "//input[@id='identifierId']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    SIGN_IN_BTN = (By.XPATH, "//*[@id='identifierId']")
    LOG_IN_BTN = (By.XPATH, "//button[text()='Log In']")
