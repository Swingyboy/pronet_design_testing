from .base_page import BasePage
from css_selectors.poker_page_locators import PokerPageLocators


class PokerPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(PokerPage, self).__init__(*args, **kwargs)

    def page_should_be_loaded(self):
        pass