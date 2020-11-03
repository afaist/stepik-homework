from selenium import webdriver
import time


link = "https://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    # Скроллим страницу так, чтобы кнока стала видимой
    # можно также проскроллить командой
    # browser.execute_script("window.scrollBy(0, 100);")
    # где 100 - это на сколько пикселей нужно проскролить вниз
    # страницу
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True

finally:
    browser.quit()
