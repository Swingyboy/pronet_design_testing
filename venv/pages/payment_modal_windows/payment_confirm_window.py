from pages.payment_modal_windows.base_window import BaseWindow

from css_selectors.payment_windows_locators.payment_confirm_window_locators import PaymentConfWinLocators


class DepositConfirmWindow(BaseWindow):

    def __init__(self, *args, **kwargs):
        super(DepositConfirmWindow, self).__init__(*args, **kwargs)

    def check_confirmation(self):
        assert self.is_element_present(*PaymentConfWinLocators.DEPOSIT_CONFIRM_MESSAGE),\
            "There is no confirmation message!"
        msg = self.browser.find_element(*PaymentConfWinLocators.DEPOSIT_CONFIRM_MESSAGE)
        assert (msg.text == "Your deposit request has been received and processed." or\
               msg.text == "Yatırım talebiniz gercekleşmiş ve işleme alınmıstır."), "Wrong confirmation message!!!"
