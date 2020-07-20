import time

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

@pytest.fixture(scope='class')
def open_login_page(browser, trader_link):
    page = MainPage(browser, trader_link[0])
    page.open()
    page.close_modal_window()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.close_modal_window()
    return login_page


class TestMainPage():

    def test_user_can_open_login_page(self, open_login_page):
        login_page = open_login_page
        login_page.login_page_should_be_loaded()


class TestLoginPage():

    def test_guest_has_incorrect_credentials(self,open_login_page):
        user = 'serhii'
        password = '!Zergswarm21'
        login_page = open_login_page
        login_page.user_login(user, password)
        login_page.wrong_credentials_message_appears()

    def test_guest_can_login(self, open_login_page):
        user = 'serhii1'
        password = '!Zergswarm22'
        login_page = open_login_page
        login_page.user_login(user, password)
        time.sleep(5)
        main_page = MainPage(login_page.browser, login_page.browser.current_url)
        main_page.user_is_logged_in(user)
