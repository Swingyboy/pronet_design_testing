from .base_page import BasePage
from css_selectors.sports_bet_page_locators import SportsBetPageLocators


class SportsBetPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(SportsBetPage, self).__init__(*args, **kwargs)

    def sports_betting_page_should_be_loaded(self):
        assert self.is_element_present(*SportsBetPageLocators.UPCOMING_EVENTS_BAR)
        assert self.is_element_present(*SportsBetPageLocators.ESPORTS_BAR)
        assert self.is_element_present(*SportsBetPageLocators.LIVE_BET_BAR)
        assert self.is_element_present(*SportsBetPageLocators.TODAY_EVENT_BAR)
        assert self.is_element_present(*SportsBetPageLocators.BET_SLIP_BAR)