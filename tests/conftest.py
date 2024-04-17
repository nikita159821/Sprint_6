from selenium import webdriver
import pytest
import sys
import os

# Добавляем путь к директории "pages"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.order_page import OrderPage
from pages.yandex_samokat_page import SamokatPage

@pytest.fixture
def browser():
    driver_browser = webdriver.Chrome()
    driver_browser.maximize_window()
    yield driver_browser
    driver_browser.quit()

@pytest.fixture
def samokat(browser):
    samokat_page = SamokatPage(browser)
    samokat_page.open()
    samokat_page.button_cookie()
    return samokat_page

@pytest.fixture
def order_page(browser):
    page = OrderPage(browser)
    page.open()
    page.button_cookie()
    return page
