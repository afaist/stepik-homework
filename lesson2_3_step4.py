from selenium import webdriver
import time
import math
import pyperclip   # для копирования в буфер обмена


"""
    Открыть страницу http://suninjuly.github.io/alert_accept.html
    Нажать на кнопку
    Принять confirm
    На новой странице решить капчу для роботов, чтобы получить число с ответом
"""
def calc(x:str)->str:
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element_by_class_name("btn-primary")
    btn.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))
    btn = browser.find_element_by_class_name("btn-primary")
    btn.click()
    time.sleep(1)
    alert = browser.switch_to.alert
    answer = alert.text.split(":")[-1]
    print(answer)
    # Копируем в буфер обмена
    pyperclip.copy(answer)

finally:
    time.sleep(5)
    browser.quit()

