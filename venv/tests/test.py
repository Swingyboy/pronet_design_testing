import time

import pytest
from pages.base_page import BasePage


class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser, trader_link):
        page = BasePage(browser, trader_link[0])
        page.open()
        page.browser.implicitly_wait(3000)
        page.go_to_login_page()
        time.sleep(10)
