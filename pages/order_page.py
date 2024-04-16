from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from tests.data import name, lastname, address
from tests.urls import URL


class OrderPage(BasePage):
    cookie = (By.ID, 'rcc-confirm-button')
    button_order = (By.CLASS_NAME, 'Button_Button__ra12g')
    name_order = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    lastname_order = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    address_order = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    metro_station_order = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')

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
    def name_order_send(self):
        self.browser.find_element(*self.name_order).send_keys(name)

    # Вводим фамилию
    def lastname_order_send(self):
        self.browser.find_element(*self.lastname_order).send_keys(lastname)

    # Вводим адрес
    def address_order_send(self):
        self.browser.find_element(*self.address_order).send_keys(address)
