from selenium.webdriver.common.by import By


class DepositPageLocators():
    PAGE_TITLE_SECTION_1 = (By.CSS_SELECTOR, 'div:nth-child(1) > div.mdl-hdr > div > span')
    PAGE_TITLE_SECTION_2 = (By.CSS_SELECTOR, 'div:nth-child(2) > div.mdl-hdr > div > span')

    BANK_TRANSFER_BTN = (By.CSS_SELECTOR, 'div.mdl-cntnt.clear > div:nth-child(2) > div > div > a')
    ACCOPAY_WALLET_BTN = (By.CSS_SELECTOR, 'div.mdl-cntnt.clear > div:nth-child(3) > div > div > a')
    ACCOPAY_ETRANSFER_BTN = (By.CSS_SELECTOR, 'div.mdl-cntnt.clear > div:nth-child(4) > div > div > a')

    CANCEL_DEPOSIT_BTN = (By.CSS_SELECTOR, 'tr:nth-child(6) > td:nth-child(2) > button')