from selenium.webdriver.common.by import By


class LiveBetPageLocators():
    GENERAL_VIEW_LINK = (By.CSS_SELECTOR, 'a.btn.left:nth-child(1)')
    MATCH_VIEW_LINK = (By.CSS_SELECTOR, 'a.btn.left:nth-child(2)')
    LIVE_BET_CALENDAR_LINK = (By.CSS_SELECTOR, 'a.btn.left:nth-child(3)')