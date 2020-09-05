from pages.base_page import BasePage
from css_selectors.virtual_sports_page_locators import VirtualSportsPageLocators


class VirtualSportsPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(VirtualSportsPage, self).__init__(*args, **kwargs)

    def page_should_be_opened(self):
        self.is_element_present(*VirtualSportsPageLocators.TITLE, timeout=20)
        title = self.browser.find_element(*VirtualSportsPageLocators.TITLE)
        assert 'Betradar Virtuals' in title.text or 'Betradar Sanallar' in title.text