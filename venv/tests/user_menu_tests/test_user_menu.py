import pytest

from pages.main_page import MainPage
from pages.deposit_page import DepositPage


class TestUserMenu():

    def test_user_can_open_deposit_page(self, login_to_page):
        main_page = MainPage(login_to_page.browser, login_to_page.browser.current_url)
        main_page.open_user_menu_page("MONEY DEPOSIT")
        deposit_page = DepositPage(main_page.browser, main_page.browser.current_url)
        deposit_page.page_should_be_opened()