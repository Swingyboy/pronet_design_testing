import time

from .base_page import BasePage
from css_selectors.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)
        
    def page_should_be_loaded(self):
        assert self.is_element_present(*LoginPageLocators.TITLE)
        assert self.is_element_present(*LoginPageLocators.USERNAME_FIELD)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD)
        assert self.is_element_present(*LoginPageLocators.NWACC_BUTTON)
        assert self.is_element_present(*LoginPageLocators.FGT_PSW_BUTTON)
        assert self.is_element_present(*LoginPageLocators.SGN_BUTTON)
        title = self.browser.find_element(*LoginPageLocators.TITLE)
        assert title.text == 'Login' or title.text == 'Giriş'

    def user_login(self, user:str, password:str):
        assert self.is_element_present(*LoginPageLocators.USERNAME_FIELD), 'The UserName field is missing!'
        user_field = self.browser.find_element(*LoginPageLocators.USERNAME_FIELD)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), 'The PAssword field is missing!'
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        user_field.clear()
        password_field.clear()
        user_field.send_keys(user)
        password_field.send_keys(password)
        time.sleep(2)
        sign_in_button = self.browser.find_element(*LoginPageLocators.SGN_BUTTON)
        sign_in_button.click()

    def wrong_credentials_message_appears(self):
        en_text = 'You have entered an incorrect username or password, please check and try again'
        tr_text = 'Yanlış kullanıcı adı veya şifre girdiniz, kontrol edip tekrar deneyin'
        assert self.is_element_present(*LoginPageLocators.ERROR_MESSAGE), f'Error message does not appear'
        error_message = self.browser.find_element(*LoginPageLocators.ERROR_MESSAGE)
        assert (error_message.text == en_text or error_message.text == tr_text), \
            f'The message {error_message.text} appears instead error message'

    def user_forgot_pswd(self):
        reset_button = self.browser.find_element(*LoginPageLocators.FGT_PSW_BUTTON)
        reset_button.click()

    def user_create_new_acc(self):
        new_acc_btn = self.browser.find_element(*LoginPageLocators.NWACC_BUTTON)
        new_acc_btn.click()

    def close_login_page(self):
        if self.is_element_clickable(*LoginPageLocators.CLOSE_BTN):
            cls_btn = self.browser.find_element(*LoginPageLocators.CLOSE_BTN)
            cls_btn.click()