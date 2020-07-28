from selenium.webdriver.common.by import By


class MainPageLocators():
    USER_MENU_BUTTON = (By.CSS_SELECTOR , '.user-name a.dropdown-button')
    SPORTS_BETTING_LINK = (By.CSS_SELECTOR, 'div.mn-menu.left > ul > li:nth-child(1)')