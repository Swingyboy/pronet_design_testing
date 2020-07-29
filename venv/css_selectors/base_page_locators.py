from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.login-btn')
    PRELOADER = (By.CSS_SELECTOR, 'div#preloader')
    MODAL_WINDOW = (By.CSS_SELECTOR, '#mdl-on-enter')
    MODAL_WINDOW_CLOSE = (By.CSS_SELECTOR, '#mdl-on-enter > a > i')
    SPORTS_BET_BTN = (By.CSS_SELECTOR, 'li[data-order="1"]')
    LIVE_BET_BTN = (By.CSS_SELECTOR, 'li[data-order="2"]')
    E_SPORTS_BET_BTN = (By.CSS_SELECTOR, 'li[data-order="3"]')
    LIVE_CASINO_BTN = (By.CSS_SELECTOR, 'li[data-order="4"]')
    CASINO_BTN = (By.CSS_SELECTOR, 'li[data-order="5"]')
    #AVIA_BTN = (By.CSS_SELECTOR, 'li[data-order="6"]')
    VIRTUAL_SPORTS_BTN = (By.CSS_SELECTOR, 'li[data-order="9"]')
    BETONGAMES_BTN = (By.CSS_SELECTOR, 'li[data-order="7"]')
    POKER_BTN = (By.CSS_SELECTOR, 'li[data-order="6"]')
    LIVE_BINGO_BTN = (By.CSS_SELECTOR, 'li[data-order="8"]')
    PROMOTIONS_BTN = (By.CSS_SELECTOR, 'li[data-order="10"]')
    AFFILIATES_BTN = (By.CSS_SELECTOR, 'li[data-order="11"]')
    HEADER_MENU_DROPDOWN_BTN = (By.CSS_SELECTOR, 'li[data-element="dropdown-wrapper"]')
    LOGO_BANNER = (By.CSS_SELECTOR, '#brand-logo')