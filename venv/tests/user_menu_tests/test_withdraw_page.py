import pytest

from pages.payment_modal_windows.bank_transfer_window import WithdrawBankTransferWin
from pages.payment_modal_windows.payment_confirm_window import DepositConfirmWindow


@pytest.mark.run(order=5)
class TestDepositPage():

    def test_user_can_create_bank_transfer_transaction(self, open_money_withdraw_page):
        page = open_money_withdraw_page
        page.open_withdraw_method("bank transfer")
        transf_win = WithdrawBankTransferWin(page.browser, page.browser.current_url)
        transf_win.create_transaction(amount=20)
