import allure

from pages.yandex_samokat_page import SamokatPage
from tests.urls import URL, URL_DZEN


class TestLogoRedirection:

    @allure.title('Проверка редиректа на домашнюю страницу')
    def test_logo_redirects_to_home(self, browser):
        samokat_page = SamokatPage(browser)
        samokat_page.open()
        samokat_page.button_cookie()

        samokat_page.logo_click()
        assert samokat_page.get_current_url() == URL

    @allure.title('Проверка редиректа на страницу Яндекс дзен')
    def test_yandex_logo_redirects_to_zen(self, browser):
        samokat_page = SamokatPage(browser)
        samokat_page.open()
        samokat_page.button_cookie()

        samokat_page.logo_yandex_click()
        samokat_page.switch_to(1)
        assert samokat_page.get_current_url() == URL_DZEN
