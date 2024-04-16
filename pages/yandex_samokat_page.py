from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from tests.urls import URL


class SamokatPage(BasePage):
    cookie = (By.ID, 'rcc-confirm-button')
    question = (By.CLASS_NAME, 'accordion__item')
    answer = (By.CSS_SELECTOR, '.accordion__panel p')

    def __init__(self, browser):
        super().__init__(browser)

    # Открываем главную страницу
    def open(self):
        self.browser.get(URL)

    # Принимаем куки
    def button_cookie(self):
        self.browser.find_element(*self.cookie).click()

    # Получаем список вопросов
    def get_questions(self):
        return self.browser.find_elements(*self.question)

    # Получаем список ответов для конкретного вопроса
    def get_answers(self, question):
        return question.find_elements(*self.answer)

    # Находим и кликаем на вопрос по индексу
    def click_question_by_index(self, index):
        questions = self.get_questions()
        # Проверяем, не пустой ли список. А также, что индекс меньше длинны списка.
        if questions and index < len(questions):
            questions[index].click()

    # Получаем текст ответа на вопрос по индексу
    def get_text_of_answer_by_index(self, index):
        questions = self.get_questions()
        # Проверяем, не пустой ли список. А также, что индекс меньше длинны списка.
        if questions and index < len(questions):
            answers = self.get_answers(questions[index])
            if answers:
                return answers[0].text

    def time(self):
        return WebDriverWait(self.browser, 30).until(expected_conditions.visibility_of_element_located(self.question))
