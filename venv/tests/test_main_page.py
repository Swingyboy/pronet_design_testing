import time

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

@pytest.mark.first
class TestMainPage():

    def test_user_can_open_login_page(self, login_page):
        lgn_page = login_page
        lgn_page.login_page_should_be_loaded()




