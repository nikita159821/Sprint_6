class TestOrder:

    def test_order_positive_top_button(self, order_page):
        order_page.order_button()
        order_page.order()
