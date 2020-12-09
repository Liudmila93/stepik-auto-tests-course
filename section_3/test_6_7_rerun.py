import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")  # запускаем один браузер для всех тестов в классе
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")

"""Сначала установим плагин в нашем виртуальном окружении. 
После установки плагин будет автоматически найден PyTest, 
и можно будет пользоваться его функциональностью без дополнительных изменений кода:

pip install pytest-rerunfailures==9.1.1
Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:

"--reruns n", где n — это количество перезапусков. 
Если при повторных запусках тесты пройдут успешно, 
то и прогон тестов будет считаться успешным. 
Количество перезапусков отображается в отчёте, 
благодаря чему можно позже анализировать проблемные тесты.
Дополнительно мы указали параметр "--tb=line", 
чтобы сократить лог с результатами теста. Можете почитать подробнее про настройку вывода в документации PyTest:"""
# pytest -v --tb=line --reruns 1 section_3/test_6_7_rerun.py