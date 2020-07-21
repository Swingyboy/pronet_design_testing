from selenium.webdriver.common.by import By


class SportsBetPageLocators():
    UPCOMING_EVENTS_BAR =(By.CSS_SELECTOR, 'upcoming-events > div > div.modul-header')
    LIVE_BET_BAR = (By.CSS_SELECTOR, 'live-at-now > div > div.modul-header')
    ESPORTS_BAR = (By.CSS_SELECTOR, 'app-esports > div > div.modul-header')
    TODAY_EVENT_BAR = (By.CSS_SELECTOR, 'todays-sport-types > div > div.modul-header')

