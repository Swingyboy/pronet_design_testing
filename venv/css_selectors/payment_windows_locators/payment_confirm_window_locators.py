from selenium.webdriver.common.by import By


class PaymentConfWinLocators():
    DEPOSIT_CONFIRM_MESSAGE = (By.CSS_SELECTOR, 'div.rslt-msg > message-box > div > div:nth-child(2)')