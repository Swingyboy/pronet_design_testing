import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilites.create_init_data import parse_csv, url_modify
from pages.base_page import BasePage
from pages.sports_bet_page import SportsBetPage


@pytest.fixture(scope='class')
def sports_betting_page(browser, trader_link):
    page = BasePage(browser, browser.current_url)
    page.go_to_top_menu_page("SPORTS BETTING")
    sport_page = SportsBetPage(browser, browser.current_url)

    yield sport_page
    sport_page.go_to_main_page()