from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

import pytest
"""
clear; pytest -s test_product_page.py
"""

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# @pytest.mark.parametrize('number', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='failed test')) for i in range(10)])
# def test_guest_can_add_product_to_basket(browser, number):
#     page = ProductPage(browser,f"{link}{number}")

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser,link)

    page.open()
    page.should_be_add_to_basket_btn()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_item_in_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    pageLogin = LoginPage(browser, link)
    pageLogin.should_be_login_page()
