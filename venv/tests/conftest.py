import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilites.create_init_data import parse_csv, url_modify
from pages.main_page import MainPage
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--path_to_csv_file', action='store', default=False, help='Specify pass to file with data')
    parser.addoption('--trader', action='store', default='makrobet', help='Specify the trader')


@pytest.fixture(scope='module')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None

    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope='class')
def trader_link(request):
    csv_file = request.config.getoption('path_to_csv_file')
    trader_name = request.config.getoption('trader')

    traders_list = parse_csv(csv_file)
    url, mobile_url = url_modify(traders_list, trader_name)
    return url, mobile_url


@pytest.fixture(scope='class')
def main_page(browser, trader_link):
    main_page = MainPage(browser, trader_link[0])
    main_page.open()
    main_page.close_modal_window()

    yield main_page
    main_page.go_to_main_page()


@pytest.fixture(scope='function')
def login_page(main_page):
    page = main_page
    page.go_to_login_page()

    login_page = LoginPage(page.browser, page.browser.current_url)
    login_page.close_modal_window()

    yield login_page
    login_page.close_login_page()


