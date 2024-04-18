from pages.base_page import BasePage

from tests.urls import URL
from locators.order_page_locators import cookie, button_order, name_order, lastname_order, address_order, \
    metro_station_order, station, telephone_order, next_button_order, delivery_order, close_calendar_order, \
    period_order, day_order, color_order, button, button_yes_order, order_is_processed, logo, logo_dzen


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
    def name_order_send(self, name_text):
        self.browser.find_element(*name_order).send_keys(name_text)

    # Вводим фамилию
    def lastname_order_send(self, lastname):
        self.browser.find_element(*lastname_order).send_keys(lastname)

    # Вводим адрес
    def address_order_send(self, address):
        self.browser.find_element(*address_order).send_keys(address)

    # Нажимаем на поле "Станция метро"
    def metro_station_click(self):
        self.browser.find_element(*metro_station_order).click()

    # Выбираем станцию "Бульвар Рокоссовского"
    def station_click(self):
        self.browser.find_element(*station).click()

    # Вводим номер телефона
    def telephone_order_send(self, telephone):
        self.browser.find_element(*telephone_order).send_keys(telephone)

    # Метод нажимает кнопку "Далее"
    def next_button_order_click(self):
        self.browser.find_element(*next_button_order).click()

    # Метод указывает дату когда привезти самокат
    def delivery_order_send(self,delivery):
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

    # Метод нажимает  на лого "Самокат"
    def logo_click(self):
        self.browser.find_element(*logo).click()

    # Метод нажимает  на лого "Яндекс"
    def logo_yandex_click(self):
        self.browser.find_element(*logo_dzen).click()

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

