from .pages.product_page import ProductPage
import pytest

"""
Chapter 4, Step 6 - Negative tests, 
clear; pytest -s test_product_page2.py

comment out implisit_wait in BasePage constructor
"""


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_item_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_item_to_basket()
    page.should_be_disappeared_success_message()

