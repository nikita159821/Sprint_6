from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.data import name, lastname, address, telephone
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
    def name_order_send(self,):
        self.browser.find_element(*self.name_order).send_keys(name)

    # Вводим фамилию
    def lastname_order_send(self,):
        self.browser.find_element(*self.lastname_order).send_keys(lastname)

    # Вводим адрес
    def address_order_send(self,):
        self.browser.find_element(*self.address_order).send_keys(address)

    # Нажимаем на поле "Станция метро"
    def metro_station_click(self,):
        self.browser.find_element(*self.metro_station_order).click()

    # Выбираем станцию "Бульвар Рокоссовского"
    def station_click(self,):
        self.browser.find_element(*self.station).click()

    # Вводим номер телефона
    def telephone_order_send(self,):
        self.browser.find_element(*self.telephone_order).send_keys(telephone)

    # Метод берет объединяет остальные меотды
    def order(self):
        self.name_order_send()
        self.lastname_order_send()
        self.address_order_send()
        self.metro_station_click()
        self.station_click()
        self.telephone_order_send()
