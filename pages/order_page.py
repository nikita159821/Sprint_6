import allure

from pages.base_page import BasePage
from locators.order_page_locators import button_order, name_order, lastname_order, address_order, \
    metro_station_order, station, telephone_order, next_button_order, delivery_order, close_calendar_order, \
    period_order, day_order, color_order, button, button_yes_order, order_is_processed, bottom_button


class OrderPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @ allure.step('Нажимаем кнопку "Заказать" в шапке')
    def order_button_click(self):
        self.find_element(*button_order).click()

    @allure.step('Нажимаем кнопку "Заказать" внизу страницы')
    def order_bottom_button_click(self):
        self.find_element(*bottom_button).click()

    @allure.step('Вводим имя')
    def name_order_send(self, name_text):
        self.find_element(*name_order).send_keys(name_text)

    @allure.step('Вводим фамилию')
    def lastname_order_send(self, lastname):
        self.find_element(*lastname_order).send_keys(lastname)

    @allure.step('Вводим адрес')
    def address_order_send(self, address):
        self.find_element(*address_order).send_keys(address)

    @allure.step('Нажимаем на поле "Станция метро')
    def metro_station_click(self):
        self.find_element(*metro_station_order).click()

    @allure.step('Выбираем станцию "Бульвар Рокоссовского')
    def station_click(self):
        self.find_element(*station).click()

    @allure.step('Вводим номер телефона')
    def telephone_order_send(self, telephone):
        self.find_element(*telephone_order).send_keys(telephone)

    @allure.step('Yажимаем кнопку "Далее"')
    def next_button_order_click(self):
        self.find_element(*next_button_order).click()

    @allure.step('Указываем дату когда привезти самокат')
    def delivery_order_send(self,delivery):
        self.find_element(*delivery_order).send_keys(delivery)

    @allure.step('Закрываем календарь')
    def close_calendar_order_click(self):
        self.find_element(*close_calendar_order).click()

    @allure.step('Нажимаем на поле "Срок аренды"')
    def period_order_click(self):
        self.find_element(*period_order).click()

    @allure.step('Выбираем срок аренды "Сутки"')
    def day_order_click(self):
        self.find_element(*day_order).click()

    @allure.step('Выбираем цвет самоката')
    def color_order_click(self):
        self.find_element(*color_order).click()

    @allure.step('Нажимаем кнопку "Заказать" под формой')
    def button_click(self):
        self.find_element(*button).click()

    @allure.step('Нажимаем кнопку "Да" в окне оформления заказ')
    def button_yes_order_click(self):
        self.find_element(*button_yes_order).click()

    # Метод возвращает "Заказ успешно оформлен"
    def return_order_is_processed(self):
        return self.find_element(*order_is_processed)

    # Метод объединяет остальные в шаг
    def order(self, customer_name, lastname, address, telephone, delivery):
        self.name_order_send(customer_name)
        self.lastname_order_send(lastname)
        self.address_order_send(address)
        self.metro_station_click()
        self.station_click()
        self.telephone_order_send(telephone)
        self.next_button_order_click()
        self.delivery_order_send(delivery)
        self.close_calendar_order_click()
        self.period_order_click()
        self.day_order_click()
        self.color_order_click()
        self.button_click()
        self.button_yes_order_click()
