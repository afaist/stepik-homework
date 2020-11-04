import pytest
from selenium import webdriver


"""
Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name, где
mark_name — произвольная строка.

Давайте разделим тесты в одном из предыдущих примеров на smoke и regression.
Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке
параметр -m и нужную метку:

pytest -s -v -m smoke test_fixture8.py

Если всё сделано правильно, то должен запуститься только тест с маркировкой smoke.
"""
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
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

