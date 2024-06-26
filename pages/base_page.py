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

    @allure.step('Нажимаем принять куки')
    # Принимаем куки
    def button_cookie(self):
        self.find_element(*cookie).click()

    @allure.step('Получаем URL открытой страницы')
    def get_current_url(self):
        return self.browser.current_url

    @allure.step('Получаем список вопросов')
    def get_questions(self):
        return self.browser.find_elements(*question)

    @allure.step('Переключаемся на вкладку')
    def switch_to(self, window_index):
        all_windows = self.browser.window_handles
        self.browser.switch_to.window(all_windows[window_index])
