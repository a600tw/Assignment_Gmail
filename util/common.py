from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 100)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        self._wait.until(ec.element_to_be_clickable(locator))
        return self

    def find(self, locator):
        self.wait_for(locator)
        element = self.driver.find_element(*locator)
        return element

    def find_elements(self, locator):
        self.wait_for(locator)
        element = self.driver.find_elements(*locator)
        return element

    def get_attribute(self, locator, attri):
        self.wait_for(locator)
        element = self.driver.find_elements(*locator)
        attribute = element.get_attribute(attri)
        return attribute

    def enter_input(self, locator, value):
        self.driver.find_element(*locator)
        self.wait_for(locator).clear()
        self.wait_for(locator).send_keys(value)
        return self
    
    def refresh_page(self):
        self.driver.refresh()
        return self


