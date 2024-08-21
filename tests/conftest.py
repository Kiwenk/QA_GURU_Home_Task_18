import pytest
from selene import browser
from utils.setup_methods import setup_for_test
import allure


@pytest.fixture(autouse=True)
def setup_browser():
    with allure.step('Конфигурация браузера'):
        browser.config.base_url = setup_for_test.url
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    setup_for_test.empty_cart()

    yield

    with allure.step('Закрытие браузера'):
        browser.quit()
