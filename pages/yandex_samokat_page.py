import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.urls import URL


class SamokatPage(BasePage):

    cookie = (By.ID,'rcc-confirm-button')
    question = (By.CLASS_NAME, 'accordion__item')

    def __init__(self, browser):
        super().__init__(browser)

    # Открываем страницу самоката
    def open(self):
        self.browser.get(URL)

    # закрываем куки
    def button(self):
        self.browser.find_element(*self.cookie).click()

    # Получаем список вопросов
    def get_questions(self):
        return self.browser.find_elements(*self.question)

    # Получаем список ответов
    #def get_answers(self):
        #test = self.browser.find_elements(*self.text)
        #print(test)

    # Выводим вопросы и ответы на экран
    def print_questions_and_answers(self):
        questions = self.get_questions()

        for question in questions:
            # Нажимаем на каждый вопрос
            question.click()
            # Делаем паузу в 5 секунд
            time.sleep(5)

