from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.login-btn')
    PRELOADER = (By.CSS_SELECTOR, 'div#preloader')