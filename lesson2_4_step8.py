from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
import pyperclip

"""

    Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    Нажать на кнопку "Book"
    Решить уже известную нам математическую задачу (используйте ранее написанный код)
    и отправить решение

Чтобы определить момент, когда цена аренды уменьшится до $100, используйте
метод text_to_be_present_in_element из библиотеки expected_conditions.
"""
def calc(x: str)->str:
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id("book")
    # ждем, пока цена не станет $100
    WebDriverWait(browser,10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    time.sleep(1)
    x = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))
    button = browser.find_element_by_id("solve")
    button.click()
    alert = browser.switch_to.alert
    answer = alert.text.split(":")[-1]
    pyperclip.copy(answer)
    print(answer)

finally:
    time.sleep(5)
    browser.quit()

