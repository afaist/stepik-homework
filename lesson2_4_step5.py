from selenium import webdriver
import time


"""
Кнопка появляется через секунду после загрузки
поэтому ставим задержку перед поиском кнопки
Улучшим наш тест с помощью неявных ожиданий. Для этого нам нужно будет убрать time.sleep()
и добавить одну строчку с методом implicitly wait:
"""
try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")
    # time.sleep(1)  задержка больше не нужна

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    browser.quit()

