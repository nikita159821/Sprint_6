from tests.urls import URL


class TestOrder:

    def test_order_positive_top_button(self, order_page):
        order_page.order_button()
        order_page.order()
        assert order_page.return_order_is_processed().is_displayed()

    def test_logo_redirects_to_home(self, order_page, browser):
        order_page.logo_click()
        assert browser.current_url == URL
