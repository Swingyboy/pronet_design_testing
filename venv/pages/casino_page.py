from .base_page import BasePage
from css_selectors.casino_page_locators import CasinoPageLocators


class CasinoPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CasinoPage, self).__init__(*args, **kwargs)

    def page_should_be_opened(self):
        self.is_element_present(*CasinoPageLocators.TITLE, timeout=20)
        title = self.browser.find_element(*CasinoPageLocators.TITLE)
        assert 'Game' in title.text or 'Oyun' in title.text