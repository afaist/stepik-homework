from selenium import webdriver
import time
import math


"""

    Открыть страницу http://suninjuly.github.io/get_attribute.html.
    Найти на ней элемент-картинку, который является изображением сундука с
    сокровищами.
    Взять у этого элемента значение атрибута valuex, которое является значением
    x для задачи.
    Посчитать математическую функцию от x (сама функция остаётся неизменной).
    Ввести ответ в текстовое поле.
    Отметить checkbox "I'm the robot".
    Выбрать radiobutton "Robots rule!".
    Нажать на кнопку "Submit".
"""
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    image = browser.find_element_by_id("treasure")
    x = image.get_attribute("valuex")
    print(x)
    txtbox = browser.find_element_by_id("answer")
    txtbox.send_keys(calc(x))
    chkbox = browser.find_element_by_id("robotCheckbox")
    chkbox.click()
    rdbtn = browser.find_element_by_id("robotsRule")
    rdbtn.click()
    btn = browser.find_element_by_class_name("btn-default")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()

