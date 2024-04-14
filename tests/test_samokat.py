import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.yandex_samokat_page import SamokatPage
from tests.urls import URL


class TestBurgerLogin:
    def test_login_to_account_main_button(self, browser):
        # создал объект класса
        samokat = SamokatPage(browser)
        # Открываем страницу
        samokat.open()
        time.sleep(10)
        samokat.button()

        samokat.print_questions_and_answers()
