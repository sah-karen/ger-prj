from .pages.main_page import MainPage
from .pages.login_page import LoginPage

#pytest -s -v --language=es .\test_main_page.py
#pytest -v --tb=line --language=en test_main_page.py

import time

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)

    page.open()
    page.should_be_login_link_    Error()
    page.go_to_login_page()
    pageLogin = LoginPage(browser, link)
    pageLogin.should_be_login_page()

