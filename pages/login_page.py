from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def input_login(self, text: str):
        elem = self.driver.find_element(By.ID, 'wpName1')
        elem.send_keys(text)
        return self

    def input_password(self, text: str):
        elem = self.driver.find_element(By.ID, 'wpPassword1')
        elem.send_keys(text)
        return self

    def click_login(self):
        elem = self.driver.find_element(By.ID, 'wpLoginAttempt')
        elem.click()
