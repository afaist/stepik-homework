from selenium import webdriver
import time
import math


"""

    Открыть страницу http://suninjuly.github.io/math.html.
    Считать значение для переменной x.
    Посчитать математическую функцию от x (код для этого приведён ниже).
    Ввести ответ в текстовое поле.
    Отметить checkbox "I'm the robot".
    Выбрать radiobutton "Robots rule!".
    Нажать на кнопку Submit.
"""
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))
    chkbox = browser.find_element_by_id("robotCheckbox")
    chkbox.click()
    rdbutton = browser.find_element_by_id("robotsRule")
    rdbutton.click()
    btn = browser.find_element_by_class_name("btn-default")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()


