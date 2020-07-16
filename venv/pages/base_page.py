import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException

from css_selectors.base_page_locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        time.sleep(5)

    def go_to_login_page(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_BUTTON, timeout=10)
        login_button = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        login_button.click()

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True