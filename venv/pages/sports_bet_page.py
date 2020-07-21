from .base_page import BasePage
from css_selectors.sports_bet_page_locators import SportsBetPageLocators


class SportsBetPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(SportsBetPage, self).__init__(*args, **kwargs)