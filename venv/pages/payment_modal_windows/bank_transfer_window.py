from time import sleep as s

from pages.payment_modal_windows.base_window import BaseWindow
from css_selectors.payment_windows_locators.bank_transfer_window_locators import DepositBankTransferLocators


class DepositBankTransferWin(BaseWindow):

    def __init__(self, *args, **kwargs):
        super(DepositBankTransferWin, self).__init__(*args, **kwargs)

    def select_bank(self, bank_position:int):
        self.open_drop_down(DepositBankTransferLocators.BANK_DROPDOWN, bank_position)

    def select_currency(self, currency_position:int):
        self.open_drop_down(DepositBankTransferLocators.CURRENCY_DROPDOWN, currency_position)

    def set_transfer_type(self, type:str):
        if type.upper() == "BANK":
            assert self.is_element_clickable(*DepositBankTransferLocators.BANK_TRANSFER_TYPE), \
                "Trasnfer type field isn't clickable!"
            self.browser.find_element(*DepositBankTransferLocators.BANK_TRANSFER_TYPE).click()
        elif type.upper() == "ATM":
            assert self.is_element_clickable(*DepositBankTransferLocators.ATM_TRANSFER_TYPE), \
                "Trasnfer type field isn't clickable!"
            self.browser.find_element(*DepositBankTransferLocators.ATM_TRANSFER_TYPE).click()
        else:
            assert False, f"There is no such type as {type}"

    def set_transfer_time(self, time:str="15:15"):
        assert self.is_element_clickable(*DepositBankTransferLocators.TRANSFER_TIME_FIELD),\
            "The timefield isn't clickable!"
        field = self.browser.find_element(*DepositBankTransferLocators.TRANSFER_TIME_FIELD)
        field.send_keys(time)

    def set_customer_note(self, note:str=""):
        assert self.is_element_clickable(*DepositBankTransferLocators.CUSTOMER_NOTE_FIELD),\
            "The customer note field isn't clickable!"
        field = self.browser.find_element(*DepositBankTransferLocators.CUSTOMER_NOTE_FIELD)
        field.send_keys(note)

    def set_amount(self, amount:int=10):
        assert self.is_element_clickable(*DepositBankTransferLocators.AMOUNT_FIELD),\
            "The amount field isn't clickable!"
        field = self.browser.find_element(*DepositBankTransferLocators.AMOUNT_FIELD)
        field.send_keys(amount)

    def finish_transaction(self):
        assert self.is_element_clickable(*DepositBankTransferLocators.FINISH_BTN),\
            "The finish button isn't clickable!"
        btn = self.browser.find_element(*DepositBankTransferLocators.FINISH_BTN)
        btn.click()

    def create_transaction(self, bank:int, type:str,
                           currency:int, time:str="15:15", amount:int=10, note:str=""):
        self.select_bank(bank)
        self.set_transfer_type(type)
        self.set_transfer_time(time)
        self.set_customer_note(note)
        self.select_currency(currency)
        self.set_amount(amount)
        self.finish_transaction()



