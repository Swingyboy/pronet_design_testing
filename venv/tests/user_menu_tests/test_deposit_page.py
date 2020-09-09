import pytest

from pages.payment_modal_windows.bank_transfer_window import DepositBankTransferWin


@pytest.mark.run(order=4)
class TestDepositPage():

    def test_user_can_create_bank_transfer_transaction(self, open_money_deposit_page):
        page = open_money_deposit_page
        page.open_deposit_method("bank transfer")
        transf_win = DepositBankTransferWin(page.browser, page.browser.current_url)
        transf_win.create_transaction(bank=1, type="bank", currency=1)

