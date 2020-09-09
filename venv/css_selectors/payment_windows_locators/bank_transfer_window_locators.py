from selenium.webdriver.common.by import By


class DepositBankTransferLocators():
    BANK_DROPDOWN = (By.CSS_SELECTOR, '#selectbank')
    BANK_TRANSFER_TYPE = (By.CSS_SELECTOR, 'div > div:nth-child(1) > label')
    ATM_TRANSFER_TYPE = (By.CSS_SELECTOR, 'div > div:nth-child(2) > label')
    TRANSFER_TIME_FIELD = (By.CSS_SELECTOR, '#transferTime')
    CUSTOMER_NOTE_FIELD = (By.CSS_SELECTOR,'#customerNote')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, '#currency')
    AMOUNT_FIELD = (By.CSS_SELECTOR, '#mntNpt')
    FINISH_BTN = (By.CSS_SELECTOR, 'form > div.input-field > button')