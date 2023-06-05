from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import TimeoutException

from pages.base_page import BasePage


class ArticlePage(BasePage):
    def is_page(self):
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="ca-nstab-main"]/a')))
            return True
        except TimeoutException:
            return False

    def click_add_to_favorite(self):
        elem = self.wait.until(ec.element_to_be_clickable((By.ID, 'ca-watch')))
        elem.click()
        self.driver.execute_script('return document.readyState;')
        # TODO: replace sleep with proper wait method
        from time import sleep
        sleep(1)
        return self
