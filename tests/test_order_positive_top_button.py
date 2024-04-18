import pytest
from tests.data import order_data
from tests.urls import URL, URL_DZEN


class TestOrder:

    @pytest.mark.parametrize('name, lastname, address, telephone, delivery', order_data)
    def test_order_positive_top_button(self, order_page, name, lastname, address, telephone, delivery):
        order_page.order_button()
        order_page.order(name, lastname, address, telephone, delivery)
        assert order_page.return_order_is_processed().is_displayed()

    def test_logo_redirects_to_home(self, order_page, browser):
        order_page.logo_click()
        assert browser.current_url == URL

    def test_yandex_logo_redirects_to_zen(self, order_page, browser):
        order_page.logo_yandex_click()
        all_windows = browser.window_handles
        browser.switch_to.window(all_windows[1])
        assert browser.current_url == URL_DZEN
