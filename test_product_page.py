from .pages.product_page import ProductPage
import time
"""
clear; pytest -s test_product_page.py
"""

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()


# def test_add_to_cart(browser):
#     page = ProductPage(url="", browser)   # инициализируем объект Page Object
#     page.open()                           # открываем страницу в браузере
#     page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
#     page.add_product_to_cart()            # жмем кнопку добавить в корзину 
#     page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом    