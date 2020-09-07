from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'div.hdr-top.clear.fix-hide > div >'
                                     ' div.logout-menu.right > ul > li:nth-child(1) > a')
    LOGO = (By.CSS_SELECTOR, 'div.hdr-top.clear.fix-hide > a')
    USER_INFO_DROP_DOWN = (By.CSS_SELECTOR, '.fix-hide > div > div.login-menu.right > ul '
                                               '> li:nth-child(1) > balance')
    USER_BALANCE_TEXT = (By.CSS_SELECTOR, '#balance-drop-top > div.balance-main > div.balance-content > '
                                          'div:nth-child(1)')

    PRELOADER = (By.CSS_SELECTOR, 'div#preloader')
    MODAL_WINDOW = (By.CSS_SELECTOR, '#mdl-on-enter')
    MODAL_WINDOW_CLOSE = (By.CSS_SELECTOR, '#mdl-on-enter > a > i')

    SPORTS_BET_BTN = (By.CSS_SELECTOR, 'li[data-order="1"]')
    LIVE_BET_BTN = (By.CSS_SELECTOR, 'li[data-order="2"]')
    JACKPOTS_BTN = (By.CSS_SELECTOR, 'li[data-order="3"]')
    E_SPORTS_BET_BTN = (By.CSS_SELECTOR, 'li[data-order="4"]')
    LIVE_CASINO_BTN = (By.CSS_SELECTOR, 'li[data-order="5"]')
    CASINO_BTN = (By.CSS_SELECTOR, 'li[data-order="6"]')
    POKER_BTN = (By.CSS_SELECTOR, 'li[data-order="7"]')
    LIVE_BINGO_BTN = (By.CSS_SELECTOR, 'li[data-order="8"]')
    BETONGAMES_BTN = (By.CSS_SELECTOR, 'li[data-order="9"]')
    VIRTUAL_SPORTS_BTN = (By.CSS_SELECTOR, 'li[data-order="10"]')
    PROMOTIONS_BTN = (By.CSS_SELECTOR, 'li[data-order="11"]')
    TOP_MENU_DROPDOWN_BTN = (By.CSS_SELECTOR, 'li[data-element="dropdown-wrapper"]')
