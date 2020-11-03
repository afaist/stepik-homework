from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


"""
Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и
дождаться, когда кнопка станет кликабельной.
Для реализации подобных ожиданий в Selenium WebDriver существует понятие явных
ожиданий (Explicit Waits), которые позволяют задать специальное ожидание для
конкретного элемента.
Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и
expected_conditions.
"""
link = "http://suninjuly.github.io/wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    browser.quit()

