from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

"""
    У каждого элемента списка обычно есть уникальное значение атрибута value
    В списках может быть разрешено выбирать как только один, так и несколько вариантов,
    в зависимости от типа списка
    Визуально списки могут различаться тем, что в одном случае все варианты
    скрыты в выпадающем меню (http://suninjuly.github.io/selects1.html),
    а в другом все варианты или их часть видны (http://suninjuly.github.io/selects2.html)

"""
# link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # 1 вариант
    # выбираем список
    # щелкаем по нему, чтобы он раскрылся
    # затем щелкаем по нужному элементу списка
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    print(num1, num2)
    sum1 = str(int(num1) + int(num2))
    print(sum1)
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='" + sum1 + "']").click()
    # 2 вариант
    # создать объект класса Select
    # и выбрать элемент с нужным текстом
#    select = Select(browser.find_element_by_tag_name("select"))
#    select.select_by_value(sum1)

    btn = browser.find_element_by_class_name("btn-default")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()

