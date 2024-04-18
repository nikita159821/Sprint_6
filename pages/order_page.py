from pages.base_page import BasePage
from tests.data import name, lastname, address, telephone, delivery
from tests.urls import URL
from locators.order_page_locators import cookie, button_order, name_order, lastname_order, address_order, \
    metro_station_order, station, telephone_order, next_button_order, delivery_order, close_calendar_order, \
    period_order, day_order, color_order, button, button_yes_order, order_is_processed


class OrderPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    # Открываем главную страницу
    def open(self):
        self.browser.get(URL)

    # Принимаем куки
    def button_cookie(self):
        self.browser.find_element(*cookie).click()

    # Нажимаем кнопку "Заказать" в шапке
    def order_button(self):
        self.browser.find_element(*button_order).click()

    # Вводим имя
    def name_order_send(self, ):
        self.browser.find_element(*name_order).send_keys(name)

    # Вводим фамилию
    def lastname_order_send(self, ):
        self.browser.find_element(*lastname_order).send_keys(lastname)

    # Вводим адрес
    def address_order_send(self, ):
        self.browser.find_element(*address_order).send_keys(address)

    # Нажимаем на поле "Станция метро"
    def metro_station_click(self, ):
        self.browser.find_element(*metro_station_order).click()

    # Выбираем станцию "Бульвар Рокоссовского"
    def station_click(self, ):
        self.browser.find_element(*station).click()

    # Вводим номер телефона
    def telephone_order_send(self, ):
        self.browser.find_element(*telephone_order).send_keys(telephone)

    # Метод нажимает кнопку "Далее"
    def next_button_order_click(self):
        self.browser.find_element(*next_button_order).click()

    # Метод указывает дату когда привезти самокат
    def delivery_order_send(self):
        self.browser.find_element(*delivery_order).send_keys(delivery)

    # Метод закрывает календарь
    def close_calendar_order_click(self):
        self.browser.find_element(*close_calendar_order).click()

    # Метод нажимает на поле "Срок аренды"
    def period_order_click(self):
        self.browser.find_element(*period_order).click()

    # Метод выбирает срок аренды "Сутки"
    def day_order_click(self):
        self.browser.find_element(*day_order).click()

    # Метот выбирает цвет самоката
    def color_order_click(self):
        self.browser.find_element(*color_order).click()

    # Метод нажимает кнопку "Заказать" под формой
    def button_click(self):
        self.browser.find_element(*button).click()

    # Метод нажимает "Да" в окне оформления заказ
    def button_yes_order_click(self):
        self.browser.find_element(*button_yes_order).click()

    # Метод возвращает "Заказ успешно оформлен"

    def return_order_is_processed(self):
        return self.browser.find_element(*order_is_processed)

    # Метод объединяет остальные в шаг
    def order(self):
        self.name_order_send()
        self.lastname_order_send()
        self.address_order_send()
        self.metro_station_click()
        self.station_click()
        self.telephone_order_send()
        self.next_button_order_click()
        self.delivery_order_send()
        self.close_calendar_order_click()
        self.period_order_click()
        self.day_order_click()
        self.color_order_click()
        self.button_click()
        self.button_yes_order_click()
