from selenium import webdriver
import time
import os

"""

    Открыть страницу http://suninjuly.github.io/file_input.html
    Заполнить текстовые поля: имя, фамилия, email
    Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    Нажать кнопку "Submit"
"""

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Ivan")
    lastname  = browser.find_element_by_name("lastname")
    lastname.send_keys("Kant")
    email    = browser.find_element_by_name("email")
    email.send_keys("test@mailo.to")
    upload   = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test.txt")
    upload.send_keys(file_path)
    btn = browser.find_element_by_class_name("btn-primary")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()

