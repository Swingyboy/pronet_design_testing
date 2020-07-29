import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.live_bet_page import LiveBetPage
from pages.live_casino_page import LiveCasinoPage
from pages.sports_bet_page import SportsBetPage


@pytest.mark.run(order=1)
class TestMainPage():

    @pytest.mark.dependency()
    def test_user_can_open_login_page(self, main_page):
        page = main_page
        page.go_to_login_page()
        lgn_page = LoginPage(page.browser, page.browser.current_url)
        lgn_page.page_should_be_loaded()
        lgn_page.close_login_page()

    def test_user_can_open_sports_bet_page(self, main_page):
        page = main_page
        page.go_to_sports_betting_page()
        sprt_bet_page = SportsBetPage(page.browser, page.browser.current_url)
        sprt_bet_page.sports_betting_page_should_be_loaded()

    def test_user_can_open_live_betting_page(self, main_page):
        page = main_page
        page.go_to_live_betting_page()
        live_bet_page = LiveBetPage(page.browser, page.browser.current_url)
        live_bet_page.live_bet_page_should_be_loaded()

    def test_user_can_open_live_casino_page(self, main_page):
        page = main_page
        page.go_to_live_casino_page()
        live_casino_page = LiveCasinoPage(page.browser, page.browser.current_url)
        live_casino_page.page_should_be_opened()

    def test_user_can_open_casino_page(self, main_page):
        pass

    def test_user_can_open_poker_page(self, main_page):
        pass

    def test_user_can_open_bet_on_games_page(self, main_page):
        pass

    def test_user_can_open_live_bingo_page(self, main_page):
        pass

    def test_user_can_open_virtual_sports_page(self, main_page):
        pass

    def test_user_can_open_promotions_page(self, main_page):
        pass

    def test_user_can_open_affilates_page(self, main_page):
        pass