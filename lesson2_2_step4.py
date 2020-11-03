from selenium import webdriver
import time


"""
Давайте попробуем вызвать alert в браузере с помощью WebDriver.
"""
try:
    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")

finally:
    time.sleep(3)
    browser.quit()

