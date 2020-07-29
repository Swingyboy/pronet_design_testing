from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException

from css_selectors.base_page_locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        assert self.is_element_disappear(*BasePageLocators.PRELOADER)

    def go_to_main_page(self):
        assert self.is_element_clickable(*BasePageLocators.LOGO_BANNER)
        logo_link = self.browser.find_element(*BasePageLocators.LOGO_BANNER)
        logo_link.click()

    def go_to_login_page(self):
        assert self.is_element_clickable(*BasePageLocators.LOGIN_BUTTON)
        button = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        button.click()

    def go_to_sports_betting_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.SPORTS_BET_BTN)
        btn = self.browser.find_element(*BasePageLocators.SPORTS_BET_BTN)
        btn.click()

    def go_to_live_betting_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.LIVE_BET_BTN)
        btn = self.browser.find_element(*BasePageLocators.LIVE_BET_BTN)
        btn.click()

    def go_to_esports_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.E_SPORTS_BET_BTN)
        btn = self.browser.find_element(*BasePageLocators.E_SPORTS_BET_BTN)
        btn.click()

    def go_to_live_casino_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.LIVE_CASINO_BTN)
        button = self.browser.find_element(*BasePageLocators.LIVE_CASINO_BTN)
        button.click()

    def go_to_casino_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.CASINO_BTN)
        btn = self.browser.find_element(*BasePageLocators.CASINO_BTN)
        btn.click()

    def go_to_poker_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.POKER_BTN)
        btn = self.browser.find_element(*BasePageLocators.POKER_BTN)
        btn.click()

    def go_to_bet_on_games_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.BETONGAMES_BTN)
        btn = self.browser.find_element(*BasePageLocators.BETONGAMES_BTN)
        btn.click()

    def go_to_live_bingo_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.LIVE_BINGO_BTN)
        btn = self.browser.find_element(*BasePageLocators.LIVE_BINGO_BTN)
        btn.click()

    def go_to_virtual_sports_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.VIRTUAL_SPORTS_BTN)
        btn = self.browser.find_element(*BasePageLocators.VIRTUAL_SPORTS_BTN)
        btn.click()

    def go_to_promotions_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.PROMOTIONS_BTN)
        btn = self.browser.find_element(*BasePageLocators.PROMOTIONS_BTN)
        btn.click()

    def go_to_affilates_page(self):
        self.open_header_menu_dropdown()
        assert self.is_element_clickable(*BasePageLocators.AFFILIATES_BTN)
        btn = self.browser.find_element(*BasePageLocators.AFFILIATES_BTN)
        btn.click()

    def open_header_menu_dropdown(self):
        if self.is_element_clickable(*BasePageLocators.HEADER_MENU_DROPDOWN_BTN):
            btn = self.browser.find_element(*BasePageLocators.HEADER_MENU_DROPDOWN_BTN)
            btn.click()

    def is_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_clickable(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_disappear(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until(EC.invisibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def close_modal_window(self):
        modal_window_present = self.is_element_present(*BasePageLocators.MODAL_WINDOW)
        if modal_window_present:
            if self.is_element_clickable(*BasePageLocators.MODAL_WINDOW_CLOSE):
                assert self.is_element_disappear(*BasePageLocators.PRELOADER)
                mdl_wnd_cls_btn = self.browser.find_element(*BasePageLocators.MODAL_WINDOW_CLOSE)
                mdl_wnd_cls_btn.click()