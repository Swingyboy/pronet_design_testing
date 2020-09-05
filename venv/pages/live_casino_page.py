from .base_page import BasePage
from css_selectors.live_casino_page_locators import LiveCasinoPageLocators


class LiveCasinoPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LiveCasinoPage, self).__init__(*args, **kwargs)

    def page_should_be_opened(self):
        self.is_element_present(*LiveCasinoPageLocators.TITLE, timeout=20)
        title = self.browser.find_element(*LiveCasinoPageLocators.TITLE)
        assert 'Game' in title.text or 'Oyun' in title.text