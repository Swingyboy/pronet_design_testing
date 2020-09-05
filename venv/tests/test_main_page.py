import pytest

from pages.affilates_page import AffilatesPage
from pages.bet_on_games_page import BetOnGamesPage
from pages.casino_page import CasinoPage
from pages.live_bet_page import LiveBetPage
from pages.live_bingo_page import LiveBingoPage
from pages.live_casino_page import LiveCasinoPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.poker_page import PokerPage
from pages.promotions_page import PromotionsPage
from pages.sports_bet_page import SportsBetPage
from pages.virtual_sports_page import VirtualSportsPage


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
        page = main_page
        page.go_to_live_casino_page()
        casino_page = CasinoPage(page.browser, page.browser.current_url)
        casino_page.page_should_be_opened()

    def test_user_can_open_poker_page(self, main_page):
        page = main_page
        page.go_to_poker_page()
        poker_page = PokerPage(page.browser, page.browser.current_url)
        poker_page.page_should_be_loaded()

    def test_user_can_open_bet_on_games_page(self, main_page):
        page = main_page
        page.go_to_bet_on_games_page()
        bog_page = BetOnGamesPage(page.browser, page.browser.current_url)
        bog_page.page_should_be_opened()

    def test_user_can_open_live_bingo_page(self, main_page):
        page = main_page
        page.go_to_live_bingo_page()
        live_bingo_page = LiveBingoPage(page.browser, page.browser.current_url)
        live_bingo_page.page_should_be_opened()

    def test_user_can_open_virtual_sports_page(self, main_page):
        page = main_page
        page.go_to_virtual_sports_page()
        virtual_sports_page = VirtualSportsPage(page.browser, page.browser.current_url)
        virtual_sports_page.page_should_be_opened()

    def test_user_can_open_promotions_page(self, main_page):
        page = main_page
        page.go_to_promotions_page()
        promo_page = PromotionsPage(page.browser, page.browser.current_url)
        promo_page.page_should_be_opened()

    @pytest.mark.skip
    def test_user_can_open_affilates_page(self, main_page):
        page = main_page
        page.go_to_affilates_page()
        aff_page = AffilatesPage(page.browser, page.browser.current_url)
        aff_page.page_should_be_opened()