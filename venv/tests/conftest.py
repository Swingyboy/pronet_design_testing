import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilites.create_init_data import parse_csv, url_modify


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--path_to_csv_file', action='store', default=False, help='Specify pass to file with data')
    parser.addoption('--trader', action='store', default='makrobet', help='Specify the trader')


@pytest.fixture(scope='class')
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