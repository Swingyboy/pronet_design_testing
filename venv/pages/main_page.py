from .base_page import BasePage

from css_selectors.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)