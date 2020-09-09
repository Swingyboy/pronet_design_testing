from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException


class BaseWindow():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_clickable(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_disappear(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until(EC.invisibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open_drop_down(self, dropdown_selector, element):
        if self.is_element_clickable(*dropdown_selector):
            dropdown = Select(self.browser.find_element(*dropdown_selector))
            dropdown.select_by_index(element)