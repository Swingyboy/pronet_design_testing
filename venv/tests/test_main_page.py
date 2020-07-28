import time

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.live_bet_page import LiveBetPage
from pages.sports_bet_page import SportsBetPage

@pytest.mark.first
class TestMainPage():

    @pytest.mark.skip
    def test_user_can_open_login_page(self, login_page):
        lgn_page = login_page
        lgn_page.login_page_should_be_loaded()

    def test_user_can_open_sports_bet_page(self, main_page):
        page = main_page
        page.open_sports_betting_page()
        sprt_bet_page = SportsBetPage(page.browser, page.browser.current_url)
        sprt_bet_page.sports_betting_page_should_be_loaded()

    def test_user_can_open_live_betting_page(self, main_page):
        page = main_page
        page.open_live_bet_page()
        live_bet_page = LiveBetPage(page.browser, page.browser.current_url)
        live_bet_page.live_bet_page_should_be_loaded()




