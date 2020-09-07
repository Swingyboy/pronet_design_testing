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
        assert self.is_element_clickable(*BasePageLocators.LOGO)
        logo_link = self.browser.find_element(*BasePageLocators.LOGO)
        logo_link.click()

    def go_to_login_page(self):
        assert self.is_element_clickable(*BasePageLocators.LOGIN_BUTTON)
        button = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        button.click()

    def go_to_top_menu_page(self, page:str):
        if page.upper() == "SPORTS BETTING":
            locator = BasePageLocators.SPORTS_BET_BTN
        elif page.upper() == "LIVE BETTING":
            locator = BasePageLocators.LIVE_BET_BTN
        elif page.upper() == "E-SPORTS":
            locator = BasePageLocators.E_SPORTS_BET_BTN
        elif page.upper() == "LIVE CASINO":
            locator = BasePageLocators.LIVE_CASINO_BTN
        elif page.upper() == "CASINO":
            locator = BasePageLocators.CASINO_BTN
        elif page.upper() == "POKER":
            locator = BasePageLocators.POKER_BTN
        elif page.upper() == "BET ON GAMES":
            locator = BasePageLocators.BETONGAMES_BTN
        elif page.upper() == "LIVE BINGO":
            locator = BasePageLocators.LIVE_BINGO_BTN
        elif page.upper() == "VIRTUAL SPORTS":
            locator = BasePageLocators.VIRTUAL_SPORTS_BTN
        elif page.upper() == "PROMOTIONS":
            locator = BasePageLocators.PROMOTIONS_BTN
        elif page.upper() == "AFFILATES":
            locator = BasePageLocators.AFFILIATES_BTN
        else:
            assert False, "There is no such element in top-menu"

        self.open_top_menu_dropdown()
        assert self.is_element_clickable(*locator), f"The {page} button isn't clickable!"
        btn = self.browser.find_element(*locator)
        btn.click()

    def open_top_menu_dropdown(self):
        if self.is_element_clickable(*BasePageLocators.TOP_MENU_DROPDOWN_BTN):
            btn = self.browser.find_element(*BasePageLocators.TOP_MENU_DROPDOWN_BTN)
            btn.click()

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_clickable(self, how, what, timeout=5):
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

    def user_is_logged_in(self, user:str):
        assert self.is_element_present(*BasePageLocators.USER_INFO_DROP_DOWN), f"The user menu is missing!!!"
        user_dropdown = self.browser.find_element(*BasePageLocators.USER_INFO_DROP_DOWN)
        user_dropdown.click()
        assert self.is_element_present(*BasePageLocators.USER_BALANCE_TEXT), f"There is no user name field"
        user_name = self.browser.find_element(*BasePageLocators.USER_BALANCE_TEXT)
        assert user in user_name.text, \
            f"The user name {user} is missing in {user_name.text}!!!!"

    def close_modal_window(self):
        modal_window_present = self.is_element_present(*BasePageLocators.MODAL_WINDOW)
        if modal_window_present:
            if self.is_element_clickable(*BasePageLocators.MODAL_WINDOW_CLOSE):
                assert self.is_element_disappear(*BasePageLocators.PRELOADER), "Modal window is still present!"
                mdl_wnd_cls_btn = self.browser.find_element(*BasePageLocators.MODAL_WINDOW_CLOSE)
                mdl_wnd_cls_btn.click()