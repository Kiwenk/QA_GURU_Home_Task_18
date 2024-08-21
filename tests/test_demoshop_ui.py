import pytest
import allure
from selene import browser, have
from utils.setup_methods import setup_for_test


@allure.tag("web")
@allure.feature("Авторизация на сайте")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_check():
    with allure.step('Проверка авторизации'):
        setup_for_test.open_browser_with_cookie()
        browser.element('.account').should(have.text('testqaigor@gmail.com'))


@allure.tag("web")
@allure.feature("Добавление товаров в корзину")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('count', [1, 2, 3])
def test_add_product_from_page_to_cart(count):
    with allure.step(f'Проверка добавления товара из страницы товара с количеством {count}'):
        setup_for_test.add_product_to_cart_from_page('31/1', count)
    with allure.step(f'Проверка количества товара в корзине - {count}'):
        setup_for_test.open_browser_with_cookie()
        browser.element('.cart-qty').should(have.text(f'({count})'))
    with allure.step(f'Проверка наименование добавленного товара'):
        browser.open('cart')
        browser.element('.product-name').should(have.text('14.1-inch Laptop'))


@allure.tag("web")
@allure.feature("Добавление товаров в корзину")
@allure.severity(allure.severity_level.NORMAL)
def test_add_product_from_main_page_to_cart():
    with allure.step('Проверка добавления товара на главной странице сайта'):
        setup_for_test.add_product_to_cart_from_main_page('31/1/1')
    with allure.step(f'Проверка количества товара в корзине - 1'):
        setup_for_test.open_browser_with_cookie()
        browser.element('.cart-qty').should(have.text(f'(1)'))
    with allure.step(f'Проверка наименование добавленного товара'):
        browser.open('cart')
        browser.element('.product-name').should(have.text('14.1-inch Laptop'))
