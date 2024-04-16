import time

from pages.order_page import OrderPage


class TestOrder:

    def test_order_positive_top_button(self, browser):
        order = OrderPage(browser)
        order.open()
        order.button_cookie()
        order.order_button()
        time.sleep(2)
        order.name_order_send()
        time.sleep(2)
        order.lastname_order_send()
        time.sleep(2)
        order.address_order_send()
        time.sleep(10)
