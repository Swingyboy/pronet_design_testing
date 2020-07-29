from .base_page import BasePage
from css_selectors.casino_page_locators import CasinoPageLocators


class CasinoPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CasinoPage, self).__init__(*args, **kwargs)

    def page_should_be_opened(self):
        pass