from selenium import webdriver
import time

"""
Чтобы получить максимальное количество баллов, прежде чем отправлять решение на
рецензию, самостоятельно убедитесь в том что:

    Тест успешно проходит на странице http://suninjuly.github.io/registration1.html﻿

    Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html

    Используемые селекторы должны быть уникальны
"""
link = "http://suninjuly.github.io/registration2.html"
try:
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
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    time.sleep(10)
    browser.quit()
