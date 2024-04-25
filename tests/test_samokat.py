import allure
import pytest

from locators.yandex_samokat_page_locators import question
from pages.yandex_samokat_page import SamokatPage
from tests.data import answer_text_1, answer_text_2, answer_text_3, answer_text_4, answer_text_5, answer_text_6, \
    answer_text_7, answer_text_8


class TestSamokat:

    @pytest.mark.parametrize("question_index, answer_index, expected_answer", [
        (0, 0, answer_text_1),
        (1, 1, answer_text_2),
        (2, 2, answer_text_3),
        (3, 3, answer_text_4),
        (4, 4, answer_text_5),
        (5, 5, answer_text_6),
        (6, 6, answer_text_7),
        (7, 7, answer_text_8)
    ])
    @allure.title('Проверка ответа на вопрос')
    def test_question_open_answer(self, browser, question_index, answer_index, expected_answer):
        samokat_page = SamokatPage(browser)
        samokat_page.open()
        samokat_page.button_cookie()

        samokat_page.click_question_by_index(question_index)
        samokat_page.wait(question)
        actual_answer = samokat_page.get_text_of_answer_by_index(answer_index)
        assert actual_answer == expected_answer
