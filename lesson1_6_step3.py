from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://sininjuly.github.io/simple_from_find_task.html"
"""
Используем блок try/finally
для закрытия браузера
"""
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    browser.quit()

