import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import cookie
from locators.yandex_samokat_page_locators import question
from tests.urls import URL


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, *args):
        return self.browser.find_element(*args)

    def wait(self, locator):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.browser.find_element(*locator)

    @allure.step('Открываем страницу')
    def open(self):
        self.browser.get(URL)

    @allure.step('Нажимае принять куки')
    # Принимаем куки
    def button_cookie(self):
        self.find_element(*cookie).click()

    # Метод возвращает URL страницы
    def get_current_url(self):
        return self.browser.current_url

    # Получаем список вопросов
    def get_questions(self):
        return self.browser.find_elements(*question)
