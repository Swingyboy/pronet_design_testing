from .base_page import BasePage
from css_selectors.forgot_password_page_locators import ForgotPswdPageLocators


class ForgotPasswordPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(ForgotPasswordPage, self).__init__(*args, **kwargs)

    def page_should_be_loaded(self):
        assert self.is_element_present(*ForgotPswdPageLocators.TITLE)
        title = self.browser.find_element(*ForgotPswdPageLocators.TITLE)
        assert title.text == 'Forgot Password' or title.text == 'Şifremi Unuttum'