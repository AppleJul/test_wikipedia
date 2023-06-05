from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    def click_article_link_by_text(self, text):
        elem = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
        elem.click()

