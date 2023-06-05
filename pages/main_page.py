from pages.base_page import BasePage
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class MainPage(BasePage):
    def is_page(self):
        return self.driver.current_url == 'https://en.wikipedia.org/wiki/Main_Page'

    def click_login(self):
        elem = self.driver.find_element(By.ID, 'pt-login-2')
        elem.click()

    def click_side_menu(self):
        elem = self.driver.find_element(By.ID, 'vector-main-menu-dropdown')
        elem.click()
        return self

    def click_random_article(self):
        elem = self.driver.find_element(By.ID, 'n-randompage')
        elem.click()

    def click_search_form(self):
        try:
            elem = self.wait.until(ec.element_to_be_clickable((By.ID, 'searchform')))
        except StaleElementReferenceException:
            elem = self.wait.until(ec.element_to_be_clickable((By.ID, 'searchform')))
        elem.click()
        return self

    def search_with_text(self, text):
        self.click_search_form()
        try:
            elem = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="searchform"]//div/input')))
            elem.send_keys(text)
            elem.send_keys(Keys.RETURN)
        except StaleElementReferenceException:
            from time import sleep
            sleep(3)
            elem = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="searchform"]//div/input')))
            elem.send_keys(text)
            elem.send_keys(Keys.RETURN)

    def click_first_article_from_news(self):
        elem = self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mp-itn"]/ul')))
        articles = elem.find_elements(By.TAG_NAME, 'a')
        articles[0].click()

    def click_watchlist(self):
        elem = self.wait.until(ec.visibility_of_element_located((By.ID, 'pt-watchlist-2')))
        elem.click()









