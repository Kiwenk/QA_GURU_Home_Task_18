import pytest
from selene import browser
from utils.setup_methods import setup_for_test


@pytest.fixture(autouse=True)
def setup_browser():
    browser.config.base_url = setup_for_test.url
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    setup_for_test.empty_cart()

    yield

    browser.close()
