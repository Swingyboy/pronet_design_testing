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
        assert self.is_element_disappear(*BasePageLocators.PRELOADER)

    def go_to_login_page(self):
        assert self.is_element_clickable(*BasePageLocators.LOGIN_BUTTON, timeout=10)
        login_button = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        login_button.click()

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

    def is_element_disappear(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until(EC.invisibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def close_modal_window(self):
        modal_window_present = self.is_element_present(*BasePageLocators.MODAL_WINDOW)
        if modal_window_present:
            if self.is_element_clickable(*BasePageLocators.MODAL_WINDOW_CLOSE):
                mdl_wnd_cls_btn = self.browser.find_element(*BasePageLocators.MODAL_WINDOW_CLOSE)
                mdl_wnd_cls_btn.click()