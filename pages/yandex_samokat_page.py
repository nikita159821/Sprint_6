import allure

from locators.yandex_samokat_page_locators import cookie, question, answer, logo_dzen, logo
from pages.base_page import BasePage


class SamokatPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Получаем список ответов для конкретного вопроса')
    def get_answers(self, question):
        return question.find_elements(*answer)

    @allure.step('Находим и кликаем на вопрос по индексу')
    def click_question_by_index(self, index):
        questions = self.get_questions()
        # Проверяем, не пустой ли список. А также, что индекс меньше длины списка.
        if questions and index < len(questions):
            questions[index].click()

    @allure.step('Получаем текст ответа на вопрос по индексу')
    def get_text_of_answer_by_index(self, index):
        questions = self.get_questions()
        # Проверяем, не пустой ли список. А также, что индекс меньше длины списка.
        if questions and index < len(questions):
            answers = self.get_answers(questions[index])
            if answers:
                return answers[0].text

    @allure.step('Нажимаем на логотип "Самокат"')
    def logo_click(self):
        self.find_element(*logo).click()

    @allure.step('Нажимаем на на логотип "Яндекс"')
    def logo_yandex_click(self):
        self.find_element(*logo_dzen).click()
