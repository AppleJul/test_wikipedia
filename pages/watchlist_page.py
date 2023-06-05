from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class WatchlistPage(BasePage):
    def get_watchlist_count(self):
        elem = self.wait.until(
            ec.visibility_of_element_located(
                (
                    By.XPATH,
                    '//*[@class="mw-rcfilters-ui-cell mw-rcfilters-ui-watchlistTopSectionWidget-watchlistDetails"]'
                )
            )
        )
        text = elem.text
        return int(text.split(' ')[2])
