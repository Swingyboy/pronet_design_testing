from selenium.webdriver.common.by import By


class WithdrawPageLocators():
    BANK_TRANSFER_BTN = (By.CSS_SELECTOR, 'div:nth-child(2) > div > div.flex-container > a')

    PAGE_TITLE_SECTION_1 = (By.CSS_SELECTOR, 'div:nth-child(1) > div.mdl-hdr > div > span')
    PAGE_TITLE_SECTION_2 = (By.CSS_SELECTOR, 'div:nth-child(2) > div.mdl-hdr > div > span')

    CANCEL_WITHDRAW_BTN = (By.CSS_SELECTOR, 'tr:nth-child(6) > td:nth-child(2) > button')