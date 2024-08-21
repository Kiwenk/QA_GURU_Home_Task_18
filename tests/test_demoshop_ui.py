import pytest
from selene import browser, be, have
from utils.setup_methods import setup_for_test


def test_login_check():
    setup_for_test.open_browser_with_cookie()
    browser.element('.account').should(have.text('testqaigor@gmail.com'))


def test_add_product_from_page_to_cart(count=3):
    setup_for_test.add_product_to_cart_from_page('31/1', count)
    setup_for_test.open_browser_with_cookie()
    browser.element('.cart-qty').should(have.text(f'({count})'))
    browser.open('cart')
    browser.element('.product-name').should(have.text('14.1-inch Laptop'))


def test_add_product_from_main_page_to_cart():
    setup_for_test.add_product_to_cart_from_main_page('31/1/1')
    setup_for_test.open_browser_with_cookie()
    browser.element('.cart-qty').should(have.text(f'(1)'))
    browser.open('cart')
    browser.element('.product-name').should(have.text('14.1-inch Laptop'))
