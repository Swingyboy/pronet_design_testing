from selenium.webdriver.common.by import By


class MainPageLocators():
    SPORTS_BETTING_LINK = (By.CSS_SELECTOR, 'div.mn-menu.left > ul > li:nth-child(1)')
    LIVE_BETTING_LINK = (By.CSS_SELECTOR, 'div.mn-menu.left > ul > li:nth-child(2)')