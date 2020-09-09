from .base_page import BasePage
from css_selectors.withdraw_page_locators import WithdrawPageLocators


class WithdrawPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(WithdrawPage, self).__init__(*args, **kwargs)

    def open_withdraw_method(self, withdraw_method:str):
        if withdraw_method.upper() == "BANK TRANSFER":
            selector = WithdrawPageLocators.BANK_TRANSFER_BTN
        else:
            assert False, f"There is no such withdraw method as {withdraw_method}"

        assert self.is_element_clickable(*selector), f"The button isn't clickable!"
        btn = self.browser.find_element(*selector)
        btn.click()

    def cancel_withdraw(self):
        assert self.is_element_clickable(*WithdrawPageLocators.CANCEL_WITHDRAW_BTN), "The cancel button isn't clickable!"
        btn = self.browser.find_element(*WithdrawPageLocators.CANCEL_WITHDRAW_BTN)
        btn.click()

    def page_should_be_opened(self):
        self.is_element_present(*WithdrawPageLocators.PAGE_TITLE_SECTION_1, timeout=20)
        title_1 = self.browser.find_element(*WithdrawPageLocators.PAGE_TITLE_SECTION_1)
        self.is_element_present(*WithdrawPageLocators.PAGE_TITLE_SECTION_2, timeout=20)
        title_2 = self.browser.find_element(*WithdrawPageLocators.PAGE_TITLE_SECTION_2)
        assert 'Withdraw' in title_1.text or 'Para Çekme' in title_1.text
        assert 'Money Withdrawal Options' in title_2.text or 'Para Çekme Seçenekleri' in title_2.text