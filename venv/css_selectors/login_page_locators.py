from selenium.webdriver.common.by import By


class LoginPageLocators():
    TITLE = (By.CSS_SELECTOR, 'div.title')
    SGN_BUTTON = (By.CSS_SELECTOR, 'button.sgn-btn')
    FGT_PSW_BUTTON = (By.CSS_SELECTOR, 'a.ftgtpass')
    NWACC_BUTTON = (By.CSS_SELECTOR, 'a.nwacc')
    USERNAME_FIELD = (By.CSS_SELECTOR, '#username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#login-password')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'message-box > div > div:nth-child(2)')