import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilites.create_init_data import parse_csv, url_modify
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.deposit_page import DepositPage


@pytest.fixture(scope='module')
def login_to_page(browser, trader_link):
    user = 'serhiibezuhlyi'
    password = 'Fabokeyy.7'

    page = BasePage(browser, trader_link[0])
    page.open_url()
    page.go_to_login_page()

    login_page = LoginPage(page.browser, page.browser.current_url)
    login_page.close_modal_window()
    login_page.user_login(user, password)
    login_page.close_login_page()

    yield page
    page.user_logout()

@pytest.fixture(scope='class')
def open_money_deposit_page(login_to_page):
    page = BasePage(login_to_page.browser, login_to_page.browser.current_url)
    page.open_user_menu_page("MONEY DEPOSIT")
    deposit_page = DepositPage(page.browser, page.browser.current_url)

    yield deposit_page
    deposit_page.go_to_main_page()