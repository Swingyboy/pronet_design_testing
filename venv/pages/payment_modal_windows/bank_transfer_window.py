from pages.payment_modal_windows.base_window import BaseWindow
from css_selectors.payment_windows_locators.bank_transfer_window_locators \
    import DepositBankTransferLocators, WithdrawBankTransferLocators


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


class WithdrawBankTransferWin(BaseWindow):

    def __init__(self, *args, **kwargs):
        super(WithdrawBankTransferWin, self).__init__(*args, **kwargs)

    def select_bank(self, bank_position:int):
        self.open_drop_down(WithdrawBankTransferLocators.BANK_DROPDOWN, bank_position)

    def select_currency(self, currency_position:int):
        self.open_drop_down(WithdrawBankTransferLocators.CURRENCY_DROPDOWN, currency_position)

    def select_identity_type(self, type:str):
        if type.upper() == "OWN":
            selector = WithdrawBankTransferLocators.OWN_ID
        elif type.upper() == "OTHER":
            selector = WithdrawBankTransferLocators.OTHER_PERSON_ID
        else:
            assert False, "Incorrect ID type!"

        self.is_element_clickable(*selector)
        btn = self.browser.find_element(*selector)
        btn.click()

    def select_id_card_type(self, type:str):
        if type.upper() == "OLD":
            selector = WithdrawBankTransferLocators.OLD_ID_CARD_TYPE
        elif type.upper() == "NEW":
            selector = WithdrawBankTransferLocators.NEW_ID_CARD_TYPE
        else:
            assert False, "Incorrect ID card type!"

        self.is_element_clickable(*selector)
        btn = self.browser.find_element(*selector)
        btn.click()

    def set_amount(self, amount:int=10):
        assert self.is_element_clickable(*WithdrawBankTransferLocators.AMOUNT_FIELD),\
            "The amount field isn't clickable!"
        field = self.browser.find_element(*WithdrawBankTransferLocators.AMOUNT_FIELD)
        field.send_keys(amount)

    def click_next_btn(self, step:int):
        if step == 1:
            selector = WithdrawBankTransferLocators.NEXT_BTN_STP_1
        elif step == 2:
            selector = WithdrawBankTransferLocators.NEXT_BTN_STP_2
        else:
            assert False, "Wrong step!"
        self.is_element_clickable(*selector)
        btn = self.browser.find_element(*selector)
        btn.click()

    def click_previous_btn(self):
        self.is_element_clickable(*WithdrawBankTransferLocators.PREVIOUS_BTN_STP_2)
        btn = self.browser.find_element(*WithdrawBankTransferLocators.PREVIOUS_BTN_STP_2)
        btn.click()

    def click_finish_btn(self):
        self.is_element_clickable(*WithdrawBankTransferLocators.FINISH_BTN)
        btn = self.browser.find_element(*WithdrawBankTransferLocators.FINISH_BTN)
        btn.click()

    def set_branch_code(self, code:int):
        assert self.is_element_clickable(*WithdrawBankTransferLocators.BRANCH_CODE_FIELD),\
            "The amount field isn't clickable!"
        field = self.browser.find_element(*WithdrawBankTransferLocators.BRANCH_CODE_FIELD)
        field.send_keys(code)

    def set_account_number(self, account:int):
        assert self.is_element_clickable(*WithdrawBankTransferLocators.ACCOUNT_NMB_FIELD),\
            "The amount field isn't clickable!"
        field = self.browser.find_element(*WithdrawBankTransferLocators.ACCOUNT_NMB_FIELD)
        field.send_keys(account)

    def set_id_number(self, id:int):
        assert self.is_element_clickable(*WithdrawBankTransferLocators.ID_NUMBER_FIELD),\
            "The ID field isn't clickable!"
        field = self.browser.find_element(*WithdrawBankTransferLocators.ID_NUMBER_FIELD)
        field.send_keys(id)

    def set_resivers_number(self, id:int):
        assert self.is_element_clickable(*WithdrawBankTransferLocators.RESIVER_ID_FIELD),\
            "The resiver's ID field isn't clickable!"
        field = self.browser.find_element(*WithdrawBankTransferLocators.RESIVER_ID_FIELD)
        field.send_keys(id)

    def set_iban_number(self, iban:str):
        assert self.is_element_clickable(*WithdrawBankTransferLocators.IBAN_FIELD),\
            "The IBAN field isn't clickable!"
        field = self.browser.find_element(*WithdrawBankTransferLocators.IBAN_FIELD)
        field.send_keys(iban)

    def set_date_field(self, date:str):
        assert self.is_element_clickable(*WithdrawBankTransferLocators.EXPIRY_DATE_FIELD),\
            "The DATE field isn't clickable!"
        field = self.browser.find_element(*WithdrawBankTransferLocators.EXPIRY_DATE_FIELD)
        field.send_keys(date)

    def set_customer_note(self, note:str):
        assert self.is_element_clickable(*WithdrawBankTransferLocators.CUSTOMER_NOTE_FIELD), \
            "The customer note field isn't clickable!"
        field = self.browser.find_element(*WithdrawBankTransferLocators.CUSTOMER_NOTE_FIELD)
        field.send_keys(note)

    def create_transaction(self, bank=1, currency=1, amount=10,
                           branch=99999, account=411111111111111111111111111111111111111111114,
                           id_type="other", iban="TR330006100519786457841326",
                           id_numb=67596269358, id_card="old", date='', note=''):
        self.select_bank(bank)
        self.select_currency(currency)
        self.set_amount(amount)
        self.click_next_btn(1)
        self.set_branch_code(branch)
        self.set_account_number(account)
        self.select_identity_type(id_type)

        if id_type.upper() == "OTHER":
            self.set_id_number(id_numb)
        elif id_type.upper() == "OWN":
            self.set_resivers_number(id_numb)
        else:
            assert False, f"Incorect IT type is selected {id_type}!"

        self.set_iban_number(iban)
        self.select_id_card_type(id_card)
        self.set_date_field(date)
        self.set_customer_note(note)
        self.click_next_btn(2)
        self.click_finish_btn()