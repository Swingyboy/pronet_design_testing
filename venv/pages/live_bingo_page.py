from pages.base_page import BasePage
from css_selectors.live_bingo_page_locators import LiveBingoPageLocators


class LiveBingoPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LiveBingoPage, self).__init__(*args, **kwargs)

    def page_should_be_opened(self):
        pass