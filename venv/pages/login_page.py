from .base_page import BasePage
from css_selectors.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)
        
    def should_be_correct_title(self):
        self.is_element_present(*LoginPageLocators.TITLE)
        title = self.browser.find_element(*LoginPageLocators.TITLE)
        assert title.text == 'Login' or title.text == 'Giriş'