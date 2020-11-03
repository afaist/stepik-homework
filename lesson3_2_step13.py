from selenium import webdriver
import time
import unittest

"""

    Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
    Создайте новый файл
    Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
    Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
    Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
    Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
    Запустите получившиеся тесты из файла
    Просмотрите отчёт о запуске и найдите последнюю строчку
    Отправьте эту строчку в качестве ответа на это задание

Информация из шага 1.6.11

Чтобы получить максимальное количество баллов, прежде чем отправлять решение на
рецензию, самостоятельно убедитесь в том что:

    Тест успешно проходит на странице http://suninjuly.github.io/registration1.html﻿

    Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html

    Используемые селекторы должны быть уникальны
"""

class TestRegistration(unittest.TestCase):
    def test_good(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        last_name.send_keys("Petrov")
        email = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        email.send_keys("test@mail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()


    def test_bad(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        last_name.send_keys("Petrov")
        email = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        email.send_keys("test@mail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()
if __name__ == "__main__":
    unittest.main()
