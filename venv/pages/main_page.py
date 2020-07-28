from .base_page import BasePage
from css_selectors.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def user_is_logged_in(self, user:str):
        assert self.is_element_present(*MainPageLocators.USER_MENU_BUTTON), f"The user menu button is missing!!!"
        user_menu_button = self.browser.find_element(*MainPageLocators.USER_MENU_BUTTON)
        assert user in user_menu_button.get_attribute('innerHTML'), \
            f"The user name {user} is missing in  {user_menu_button.get_attribute('innerHTML')}!!!!"

    def open_sports_betting_page(self):
        assert self.is_element_clickable(*MainPageLocators.SPORTS_BETTING_LINK)
        link = self.browser.find_element(*MainPageLocators.SPORTS_BETTING_LINK)
        link.click()

    def open_live_bet_page(self):
        assert self.is_element_clickable(*MainPageLocators.LIVE_BETTING_LINK)
        link = self.browser.find_element(*MainPageLocators.LIVE_BETTING_LINK)
        link.click()