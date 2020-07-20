import time

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLoginFromMainPage():

    def test_guest_has_incorrect_credentials(self, browser, trader_link):
        user = 'serhii'
        password = '!Zergswarm21'
        page = MainPage(browser, trader_link[0])
        page.open()
        page.close_modal_window()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.close_modal_window()
        login_page.login_page_should_be_loaded()
        login_page.user_login(user, password)
        login_page.wrong_credentials_message_appears()

    def test_guest_can_login(self, browser, trader_link):
        user = 'serhii'
        password = '!Zergswarm22'
        page = MainPage(browser, trader_link[0])
        page.open()
        page.close_modal_window()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.close_modal_window()
        login_page.login_page_should_be_loaded()
        login_page.user_login(user, password)
        page.user_is_logged_in(user)




