from selenium import webdriver
import time


"""
Какую ошибку вы увидите в консоле при
если попытаетесь выполнить команду browser.find_element_by_id("button")
после открытия страницы http://suninjuly.github.io/cats.html?
"""
try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get("hhttp://suninjuly.github.io/cats.html")

    button = browser.find_element_by_id("button")
    button.click()

finally:
    browser.quit()

