import time

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser, trader_link):
        page = MainPage(browser, trader_link[0])
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_correct_title()
        time.sleep(10)
