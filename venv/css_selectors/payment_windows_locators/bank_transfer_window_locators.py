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


class WithdrawBankTransferLocators():
    ACCOUNT_NMB_FIELD = (By.CSS_SELECTOR, '#accountNumber')
    AMOUNT_FIELD = (By.CSS_SELECTOR, '#mntNpt')
    BANK_DROPDOWN = (By.CSS_SELECTOR, '#selectbank')
    BRANCH_CODE_FIELD = (By.CSS_SELECTOR, '#bankBranch')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, '#currency')
    CUSTOMER_NOTE_FIELD = (By.CSS_SELECTOR, '#customerNote')
    EXPIRY_DATE_FIELD = (By.CSS_SELECTOR, '#accountDate')
    ID_NUMBER_FIELD = (By.CSS_SELECTOR, '#relativeIdentity')
    IBAN_FIELD = (By.CSS_SELECTOR, '#iban')
    RESIVER_ID_FIELD = (By.CSS_SELECTOR, '#buyerIdentity')

    OTHER_PERSON_ID = (By.CSS_SELECTOR, '#PaymentFormModal div:nth-child(4) div:nth-child(1) > label')
    OWN_ID = (By.CSS_SELECTOR, '#PaymentFormModal div:nth-child(4) div:nth-child(2) > label')
    OLD_ID_CARD_TYPE = (By.CSS_SELECTOR, '#PaymentFormModal div:nth-child(8) div:nth-child(1) > label')
    NEW_ID_CARD_TYPE = (By.CSS_SELECTOR, '#PaymentFormModal div:nth-child(8) div:nth-child(2) > label')

    NEXT_BTN_STP_1 = (By.CSS_SELECTOR, 'form > div.input-field > button')
    NEXT_BTN_STP_2 = (By.CSS_SELECTOR, 'div:nth-child(2) > div > button')
    PREVIOUS_BTN_STP_2 = (By.CSS_SELECTOR, 'div:nth-child(1) > div > button')
    FINISH_BTN = (By.CSS_SELECTOR, '#PaymentFormModal button')