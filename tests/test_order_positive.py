import allure
import pytest
from tests.data import order_data_top_button, order_data_bottom_button


class TestOrder:

    @allure.title('Проверка оформления заказа через кнопку в шапке сайта')
    @pytest.mark.parametrize('name, lastname, address, telephone, delivery', order_data_top_button)
    def test_order_positive_top_button(self, order_page, name, lastname, address, telephone, delivery):
        order_page.order_button_click()
        order_page.order(name, lastname, address, telephone, delivery)
        assert order_page.return_order_is_processed().is_displayed()

    @allure.title('Проверка оформления заказа через кнопку в нижней части страницы')
    @pytest.mark.parametrize('name, lastname, address, telephone, delivery', order_data_bottom_button)
    def test_order_scooter_from_bottom_button(self, order_page, name, lastname, address, telephone, delivery):
        order_page.order_bottom_button_click()
        order_page.order(name, lastname, address, telephone, delivery)
        assert order_page.return_order_is_processed().is_displayed()
