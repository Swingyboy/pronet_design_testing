import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.nw_acc_page import NwAccPage
from pages.forgot_password_page import ForgotPasswordPage


@pytest.mark.run(order=2)
@pytest.mark.dependency(depends=['test_main_page.py::TestMainPage::test_user_can_open_login_page'],
                        scope='session')
class TestLoginPage():

    def test_user_has_incorrect_credentials(self, login_page):
        user = 'serhii12'
        password = '!Zergswarm21'
        lgn_page = login_page
        lgn_page.page_should_be_loaded()
        lgn_page.user_login(user, password)
        lgn_page.wrong_credentials_message_appears()

    def test_user_can_open_reset_password(self, login_page):
        lgn_page = login_page
        lgn_page.page_should_be_loaded()
        lgn_page.user_forgot_pswd()
        fgt_pswd_page = ForgotPasswordPage(lgn_page.browser, lgn_page.browser.current_url)
        fgt_pswd_page.page_should_be_loaded()
        fgt_pswd_page.go_to_main_page()

    def test_user_can_open_new_account(self, login_page):
        lgn_page = login_page
        lgn_page.page_should_be_loaded()
        lgn_page.user_create_new_acc()
        new_acc_page = NwAccPage(lgn_page.browser, lgn_page.browser.current_url)
        new_acc_page.page_should_be_loaded()
        new_acc_page.go_to_main_page()

    @pytest.mark.xfail
    def test_user_can_login(self, login_page):
        user = 'serhii'
        password = '!Fabokeyy.7'
        lgn_page = login_page
        lgn_page.page_should_be_loaded()
        lgn_page.user_login(user, password)
        main_page = MainPage(lgn_page.browser, lgn_page.browser.current_url)
        main_page.user_is_logged_in(user)