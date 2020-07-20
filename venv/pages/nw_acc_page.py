from .base_page import BasePage
from css_selectors.nw_acc_page_locators import NwAccPageLocators


class NwAccPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(NwAccPage, self).__init__(*args, **kwargs)

    def page_should_be_loaded(self):
        assert self.is_element_present(*NwAccPageLocators.TITLE)
        title = self.browser.find_element(*NwAccPageLocators.TITLE)
        assert title.text == 'Register' or title.text == 'Üye Ol'