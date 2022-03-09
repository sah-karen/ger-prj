from selenium import webdriver
from selenium.webdriver.common.by import By

#pytest -s -v --language=es .\test_items.py


import time

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    go_to_login_page(browser)
    time.sleep(5)
