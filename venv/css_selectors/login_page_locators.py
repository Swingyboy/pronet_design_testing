from selenium.webdriver.common.by import By


class LoginPageLocators():
    TITLE = (By.CSS_SELECTOR, '.login-form div.title')
    SGN_BUTTON = (By.CSS_SELECTOR, 'button.sgn-btn')
    FGT_PSW_BUTTON = (By.CSS_SELECTOR, 'a.ftgtpass')
    NWACC_BUTTON = (By.CSS_SELECTOR, 'a.nwacc')
    USERNAME_FIELD = (By.CSS_SELECTOR, 'form.login-form #username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#login-password')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'message-box > div > div:nth-child(2)')
    CLOSE_BTN = (By.CSS_SELECTOR, '#sgn-mdl > a > i')