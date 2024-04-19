import allure

from locators.yandex_samokat_page_locators import question
from tests.data import answer_text_1, answer_text_2, answer_text_3, answer_text_4, answer_text_5, answer_text_6, \
    answer_text_7, answer_text_8


class TestSamokat:

    @allure.title('Проверка первого ответа на вопрос')
    def test_question_1_open_answer(self, samokat):
        samokat.click_question_by_index(0)
        samokat.wait(question)
        answer_1 = samokat.get_text_of_answer_by_index(0)
        assert answer_1 == answer_text_1

    @allure.title('Проверка второго ответа на вопрос')
    def test_question_2_open_answer(self, samokat):
        samokat.click_question_by_index(1)
        samokat.wait(question)
        answer_2 = samokat.get_text_of_answer_by_index(1)
        assert answer_2 == answer_text_2

    @allure.title('Проверка третьего ответа на вопрос')
    def test_question_3_open_answer(self, samokat):
        samokat.click_question_by_index(2)
        samokat.wait(question)
        answer_3 = samokat.get_text_of_answer_by_index(2)
        assert answer_3 == answer_text_3

    @allure.title('Проверка четвертого ответа на вопрос')
    def test_question_4_open_answer(self, samokat):
        samokat.click_question_by_index(3)
        samokat.wait(question)
        answer_4 = samokat.get_text_of_answer_by_index(3)
        assert answer_4 == answer_text_4

    @allure.title('Проверка пятого ответа на вопрос')
    def test_question_5_open_answer(self, samokat):
        samokat.click_question_by_index(4)
        samokat.wait(question)
        answer_5 = samokat.get_text_of_answer_by_index(4)
        assert answer_5 == answer_text_5

    @allure.title('Проверка шестого ответа на вопрос')
    def test_question_6_open_answer(self, samokat):
        samokat.click_question_by_index(5)
        samokat.wait(question)
        answer_6 = samokat.get_text_of_answer_by_index(5)
        assert answer_6 == answer_text_6

    @allure.title('Проверка седьмого ответа на вопрос')
    def test_question_7_open_answer(self, samokat):
        samokat.click_question_by_index(6)
        samokat.wait(question)
        answer_7 = samokat.get_text_of_answer_by_index(6)
        assert answer_7 == answer_text_7

    @allure.title('Проверка восьмого ответа на вопрос')
    def test_question_8_open_answer(self, samokat):
        samokat.click_question_by_index(7)
        samokat.wait(question)
        answer_8 = samokat.get_text_of_answer_by_index(7)
        assert answer_8 == answer_text_8
