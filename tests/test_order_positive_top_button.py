from pages.order_page import OrderPage


class TestOrder:

    def test_order_positive_top_button(self, browser):
        order = OrderPage(browser)
        order.open()
        order.button_cookie()
        order.order_button()
        order.order()
