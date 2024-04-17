import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.data import name, lastname, address, telephone, delivery
from tests.urls import URL


class OrderPage(BasePage):
    cookie = (By.ID, 'rcc-confirm-button')
    button_order = (By.CLASS_NAME, 'Button_Button__ra12g')
    name_order = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    lastname_order = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    address_order = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    metro_station_order = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    station = (By.CSS_SELECTOR, 'div.Order_Text__2broi')
    telephone_order = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')
    next_button_order = (By.XPATH, "//button[text()='Далее']")
    delivery_order = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    period_order = (By.CSS_SELECTOR, '.Dropdown-placeholder')
    day_order = (By.XPATH, "//div[@class='Dropdown-option'and text()='сутки']")
    color_order = (By.ID, 'black')
    button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    close_calendar_order = (By.XPATH, "//div[@class='App_App__15LM-']")
    button_yes_order = (By.XPATH, "//button[text()='Да']")
    order_is_processed = (By.XPATH, "//div[@class='Order_Text__2broi']")

    def __init__(self, browser):
        super().__init__(browser)

    # Открываем главную страницу
    def open(self):
        self.browser.get(URL)

    # Принимаем куки
    def button_cookie(self):
        self.browser.find_element(*self.cookie).click()

    # Нажимаем кнопку "Заказать" в шапке
    def order_button(self):
        self.browser.find_element(*self.button_order).click()

    # Вводим имя
    def name_order_send(self, ):
        self.browser.find_element(*self.name_order).send_keys(name)

    # Вводим фамилию
    def lastname_order_send(self, ):
        self.browser.find_element(*self.lastname_order).send_keys(lastname)

    # Вводим адрес
    def address_order_send(self, ):
        self.browser.find_element(*self.address_order).send_keys(address)

    # Нажимаем на поле "Станция метро"
    def metro_station_click(self, ):
        self.browser.find_element(*self.metro_station_order).click()

    # Выбираем станцию "Бульвар Рокоссовского"
    def station_click(self, ):
        self.browser.find_element(*self.station).click()

    # Вводим номер телефона
    def telephone_order_send(self, ):
        self.browser.find_element(*self.telephone_order).send_keys(telephone)

    # Метод нажимает кнопку "Далее"
    def next_button_order_click(self):
        self.browser.find_element(*self.next_button_order).click()

    # Метод указывает дату когда привезти самокат
    def delivery_order_send(self):
        self.browser.find_element(*self.delivery_order).send_keys(delivery)

    # Метод закрывает календарь
    def close_calendar_order_click(self):
        self.browser.find_element(*self.close_calendar_order).click()

    # Метод нажимает на поле "Срок аренды"
    def period_order_click(self):
        self.browser.find_element(*self.period_order).click()

    # Метод выбирает срок аренды "Сутки"
    def day_order_click(self):
        self.browser.find_element(*self.day_order).click()

    # Метот выбирает цвет самоката
    def color_order_click(self):
        self.browser.find_element(*self.color_order).click()

    # Метод нажимает кнопку "Заказать" под формой
    def button_click(self):
        self.browser.find_element(*self.button).click()

    # Метод нажимает "Да" в окне оформления заказ
    def button_yes_order_click(self):
        self.browser.find_element(*self.button_yes_order).click()

    # Метод возвращает "Заказ успешно оформлен"

    def return_order_is_processed(self):
        return self.browser.find_element(*self.order_is_processed)

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
