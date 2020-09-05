from .base_page import BasePage
from css_selectors.sports_bet_page_locators import SportsBetPageLocators


class SportsBetPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(SportsBetPage, self).__init__(*args, **kwargs)

    def sports_betting_page_should_be_loaded(self):
        assert self.is_element_present(*SportsBetPageLocators.UPCOMING_EVENTS_BAR)
        #assert self.is_element_present(*SportsBetPageLocators.ESPORTS_BAR)
        assert self.is_element_present(*SportsBetPageLocators.LIVE_BET_BAR)
        assert self.is_element_present(*SportsBetPageLocators.TODAY_EVENT_BAR)
        title_1 = self.browser.find_element(*SportsBetPageLocators.UPCOMING_EVENTS_BAR).text
        #title_2 = self.browser.find_element(*SportsBetPageLocators.ESPORTS_BAR).text
        title_3 = self.browser.find_element(*SportsBetPageLocators.LIVE_BET_BAR).text
        title_4 = self.browser.find_element(*SportsBetPageLocators.TODAY_EVENT_BAR).text
        assert 'Upcoming Events' in title_1 or 'Birazdan Oynanacaklar' in title_1
        #assert 'E-Sports' in title_2 or 'E-sport' in title_2
        assert 'Live Bet' in title_3 or 'Canlı' in title_3
        assert "Today's Events" in title_4 or 'Günün Maçları' in title_4