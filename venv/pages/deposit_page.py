from .base_page import BasePage
from css_selectors.deposit_page_locators import DepositPageLocators


class DepositPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(DepositPage, self).__init__(*args, **kwargs)

    def open_deposit_method(self, deposit_method:str):
        if deposit_method.upper() == "BANK TRANSFER":
            selector = DepositPageLocators.BANK_TRANSFER_BTN
        elif deposit_method.upper() == "ACCOPAY WALLET":
            selector = DepositPageLocators.ACCOPAY_WALLET_BTN
        elif deposit_method.upper() == "ACCOPAY INTERACT E-TRANSFER":
            selector = DepositPageLocators.ACCOPAY_ETRANSFER_BTN
        else:
            assert False, f"There is no such deposit method as {deposit_method}"

        assert self.is_element_clickable(*selector), f"The button isn't clickable!"
        btn = self.browser.find_element(*selector)
        btn.click()

    def page_should_be_opened(self):
        self.is_element_present(*DepositPageLocators.PAGE_TITLE_SECTION_1, timeout=20)
        title_1 = self.browser.find_element(*DepositPageLocators.PAGE_TITLE_SECTION_1)
        self.is_element_present(*DepositPageLocators.PAGE_TITLE_SECTION_2, timeout=20)
        title_2 = self.browser.find_element(*DepositPageLocators.PAGE_TITLE_SECTION_2)
        assert 'Deposit' in title_1.text or 'Para Yatırma' in title_1.text
        assert 'Money Deposit Options' in title_2.text or 'Para Yatırma Seçenekleri' in title_2.text
