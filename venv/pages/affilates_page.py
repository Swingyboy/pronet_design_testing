from .base_page import BasePage
from css_selectors.affilates_page_locators import AffilatesPageLocators


class AffilatesPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(AffilatesPage, self).__init__(*args, **kwargs)

    def page_should_be_opened(self):
        pass