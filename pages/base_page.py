from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://en.wikipedia.org"

    def open_page(self, text=""):
        self.driver.get(f"{self.base_url}{text}")
        return self
