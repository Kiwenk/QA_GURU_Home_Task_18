import os
import json
import logging
import allure
from allure_commons.types import AttachmentType
import requests
from selene import browser, be
from dotenv import load_dotenv


class SetupMethods:
    def __init__(self):
        self.url = 'https://demowebshop.tricentis.com/'

        load_dotenv()
        self.login = os.getenv('LOGIN')
        self.password = os.getenv('PASSWORD')

    def authorization_api_style_with_cookies(self):
        with allure.step('Авторизация на сайте'):
            result = requests.post(
                url=self.url + "/login",
                data={"Email": self.login, "Password": self.password, "RememberMe": False},
                allow_redirects=False
            )
        cookies = result.cookies.get("NOPCOMMERCE.AUTH")
        return cookies

    def open_browser_with_cookie(self):
        with allure.step('Открытие браузера'):
            cookie = self.authorization_api_style_with_cookies()
            browser.open('')
            browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
            browser.driver.refresh()

    def empty_cart(self):
        with allure.step('Очистка корзины'):
            self.open_browser_with_cookie()
            browser.open('cart')
            if browser.element('.update-cart-button').matching(be.clickable):
                for cart in browser.all('[name="removefromcart"]'):
                    cart.click()
                browser.element('.update-cart-button').click()
            else:
                pass

    def add_product_to_cart_from_page(self, product_number, count):
        with allure.step('Добавление товара на главной странице'):
            cookies = self.authorization_api_style_with_cookies()
            response = requests.post(url=self.url + f'/addproducttocart/details/{product_number}',
                                     data={'addtocart_31.EnteredQuantity': f'{count}'},
                                     cookies={'NOPCOMMERCE.AUTH': cookies})
            if response.status_code != 200:
                raise ValueError("Response code is not 200")

            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                          attachment_type=AttachmentType.JSON, extension="json")
            logging.info(response.request.url)
            logging.info(response.status_code)
            logging.info(response.text)

            return response.status_code

    def add_product_to_cart_from_main_page(self, product_number):
        with allure.step('Добавление товара на странице товара'):
            cookies = self.authorization_api_style_with_cookies()
            response = requests.post(url=self.url + f'/addproducttocart/catalog/{product_number}',
                                     cookies={'NOPCOMMERCE.AUTH': cookies})
            if response.status_code != 200:
                raise ValueError("Response code is not 200")

            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                          attachment_type=AttachmentType.JSON, extension="json")
            logging.info(response.request.url)
            logging.info(response.status_code)
            logging.info(response.text)

            return response.status_code


setup_for_test = SetupMethods()
