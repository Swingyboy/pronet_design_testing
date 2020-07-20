from selenium.webdriver.common.by import By


class ForgotPswdPageLocators():
    TITLE = (By.CSS_SELECTOR, 'div#forgot-password h4')
    USER_NAME_BTN = (By.CSS_SELECTOR, 'input#for-username')
    EMAIL_BTN = (By.CSS_SELECTOR, 'input#for-email')
    INPUT_FIELD = (By.CSS_SELECTOR, 'input.validate')
    SEND_BTN = (By.CSS_SELECTOR, 'button.login-btn')