from tests.urls import URL, URL_DZEN


class TestLogoRedirection:
    def test_logo_redirects_to_home(self, samokat, browser):
        samokat.logo_click()
        assert browser.current_url == URL

    def test_yandex_logo_redirects_to_zen(self, samokat, browser):
        samokat.logo_yandex_click()
        all_windows = browser.window_handles
        browser.switch_to.window(all_windows[1])
        assert browser.current_url == URL_DZEN
