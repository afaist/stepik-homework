from selenium import webdriver
import time
import math       # Для решения задачи
import pyperclip  # Для копирования ответа в буфер обмена


"""
    Открыть страницу http://suninjuly.github.io/redirect_accept.html
    Нажать на кнопку
    Переключиться на новую вкладку
    Пройти капчу для робота и получить число-ответ
"""
def calc(x:str)->str:
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element_by_class_name("btn-primary")
    btn.click()
    # Должна появиться новая вкладка
    # переключаемся на нее
    # Считаем, что она вторая (индекс 1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    print(browser.title)
    x = browser.find_element_by_id("input_value").text
    txt = browser.find_element_by_id("answer")
    txt.send_keys(calc(x))
    btn = browser.find_element_by_class_name("btn-primary")
    btn.click()
    alert = browser.switch_to.alert()
    answer = alert.text.split(":")[-1]
    print(answer)
    pyperclip.copy(answer)

finally:
    time.sleep(9)
    browser.quit()

