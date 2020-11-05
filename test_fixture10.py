import pytest
from selenium import webdriver


"""
Теперь добавим в наш тестовый класс тест, который проверяет наличие кнопки
"Избранное":

def test_guest_should_see_search_button_on_the_main_page(self, browser):
     browser.get(link)
     browser.find_element_by_css_selector("button.favorite")

Предположим, что такая кнопка должна быть, но из-за изменений в коде она
пропала. Пока разработчики исправляют баг, мы хотим, чтобы результат прогона
﻿всех ﻿наших тестов был успешен, но падающий тест помечался
соответствующим образом, чтобы про него не забыть. Добавим маркировку
@pytest.mark.xfail для падающего теста.
"""
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")

