import allure
from tests.urls import URL, URL_DZEN


class TestLogoRedirection:

    @allure.title('Проверка редиректа на домашнюю страницу')
    def test_logo_redirects_to_home(self, samokat, browser):
        samokat.logo_click()
        assert samokat.get_current_url() == URL

    @allure.title('Проверка редиректа на страницу Яндекс дзен')
    def test_yandex_logo_redirects_to_zen(self, samokat, browser):
        samokat.logo_yandex_click()
        samokat.switch_to(1)
        assert samokat.get_current_url() == URL_DZEN
