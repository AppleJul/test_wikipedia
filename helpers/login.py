import os

from pages.login_page import LoginPage
from pages.main_page import MainPage

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


def login_user(driver, login=LOGIN, password=PASSWORD):
    MainPage(driver).click_login()

    LoginPage(driver)\
        .input_login(login)\
        .input_password(password)\
        .click_login()