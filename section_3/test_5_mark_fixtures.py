import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")  # заведомо падающий
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")

# pytest -s -v -m smoke section_3/test_5_mark_fixtures.py
# pytest -s -v -m "not smoke" section_3/test_5_mark_fixtures.py   - все тесты кроме smoke
# pytest -s -v -m "smoke or regression" section_3/test_5_mark_fixtures.py    - выбираем тесты
# pytest -s -v -m "smoke and win10" section_3/test_5_mark_fixtures.py   - сочетание меток
#  @pytest.mark.skip  - для пропуска теста
# pytest -rx -v test_fixture10a.py    - для отображения причины для XFAIL

