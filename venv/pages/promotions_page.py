from pages.base_page import BasePage
from css_selectors.promotions_page_locators import PromotionPageLocators


class PromotionsPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(PromotionsPage, self).__init__(*args, **kwargs)

    def page_should_be_opened(self):
        self.is_element_present(*PromotionPageLocators.TITLE, timeout=20)
        title = self.browser.find_element(*PromotionPageLocators.TITLE)
        assert 'PROMOSYONLAR' in title.text or 'PROMOSYONLAR' in title.text