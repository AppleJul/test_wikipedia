from helpers.login import login_user
from pages.article_page import ArticlePage
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.watchlist_page import WatchlistPage


def test_log_in(start_page):
    driver = start_page
    login_user(start_page)
    assert MainPage(driver).is_page()


def test_search(start_page):
    driver = start_page
    MainPage(driver)\
        .click_search_form()\
        .search_with_text('Bernau')
    SearchPage(driver).click_article_link_by_text('Bernau bei Berlin')

    assert driver.current_url == 'https://en.wikipedia.org/wiki/Bernau_bei_Berlin'


def test_random_article(start_page):
    driver = start_page
    MainPage(driver)\
        .click_side_menu()\
        .click_random_article()
    assert ArticlePage(driver).is_page()


def test_open_article_from_news(start_page):
    driver = start_page
    MainPage(driver).click_first_article_from_news()
    assert ArticlePage(driver).is_page()


def test_add_watchlist(start_page):
    driver = start_page
    login_user(driver)
    MainPage(driver).click_watchlist()
    before = WatchlistPage(driver).get_watchlist_count()
    MainPage(driver).click_random_article()
    ArticlePage(driver).click_add_to_favorite()
    after = WatchlistPage(driver) \
        .open_page('/wiki/Special:Watchlist') \
        .get_watchlist_count()
    assert after - before == 1
