from .base_page import BasePage
from css_selectors.bet_on_games_page_locators import BetOnGamesPageLocators


class BetOnGamesPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(BetOnGamesPage, self).__init__(*args, **kwargs)

    def page_should_be_opened(self):
        self.is_element_present(*BetOnGamesPageLocators.TITLE, timeout=20)
        title = self.browser.find_element(*BetOnGamesPageLocators.TITLE)
        assert 'Betongames' in title.text or 'Betongames' in title.text