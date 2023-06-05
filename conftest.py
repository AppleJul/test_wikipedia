import pytest
from selenium import webdriver


@pytest.fixture
def start_page():
    driver = webdriver.Chrome()
    driver.get("https://en.wikipedia.org")
    yield driver
    driver.close()
    driver.quit()
