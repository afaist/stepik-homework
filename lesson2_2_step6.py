from selenium import webdriver
import time
import math

"""

    Открыть страницу http://SunInJuly.github.io/execute_script.html.
    Считать значение для переменной x.
    Посчитать математическую функцию от x.
    Проскроллить страницу вниз.
    Ввести ответ в текстовое поле.
    Выбрать checkbox "I'm the robot".
    Переключить radiobutton "Robots rule!".
    Нажать на кнопку "Submit".
"""
def calc(x):
    """
    Вычисляет значение функции, заданной на странице
    Параметры:
        x - целое число, представленное строкой
    Возвращает:
        строку с вычисленным значением
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


def scrollIntoView(element):
    """
    Скролит страницу так, чтобы переданный элемент был виден на экране
    """
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)


link = "http://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    input_box = browser.find_element_by_id("answer")
    # На всякий случай делаем его видимым
    scrollIntoView(input_box)
    input_box.send_keys(calc(x))
    chkboxRobot = browser.find_element_by_id("robotCheckbox")
    scrollIntoView(chkboxRobot)
    chkboxRobot.click()
    rdbRobot = browser.find_element_by_id("robotsRule")
    scrollIntoView(rdbRobot)
    rdbRobot.click()
    btn = browser.find_element_by_class_name("btn-primary")
    scrollIntoView(btn)
    btn.click()

finally:
    time.sleep(5)
    browser.quit()

