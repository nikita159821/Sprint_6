import pytest
from tests.data import order_data


class TestOrder:

    @pytest.mark.parametrize('name, lastname, address, telephone, delivery', order_data)
    def test_order_positive_top_button(self, order_page, name, lastname, address, telephone, delivery):
        order_page.order_button()
        order_page.order(name, lastname, address, telephone, delivery)
        assert order_page.return_order_is_processed().is_displayed()
