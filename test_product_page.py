from .pages.product_page import ProductPage
import pytest
"""
clear; pytest -s test_product_page.py
"""

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('number', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='failed test')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, number):
    page = ProductPage(browser,f"{link}{number}")
    #page = ProductPage(browser,link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_item_in_basket()

# def test_add_to_cart(browser):
#     page = ProductPage(url="", browser)   # инициализируем объект Page Object
#     page.open()                           # открываем страницу в браузере
#     page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
#     page.add_product_to_cart()            # жмем кнопку добавить в корзину 
#     page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом    