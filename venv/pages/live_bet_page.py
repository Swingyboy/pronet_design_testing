from .base_page import BasePage
from css_selectors.live_bet_page_locators import LiveBetPageLocators


class LiveBetPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LiveBetPage, self).__init__(*args, **kwargs)

    def live_bet_page_should_be_loaded(self):
        self.is_element_clickable(*LiveBetPageLocators.GENERAL_VIEW_LINK)
        self.is_element_clickable(*LiveBetPageLocators.LIVE_BET_CALENDAR_LINK)
        self.is_element_clickable(*LiveBetPageLocators.MATCH_VIEW_LINK)