from selenium import webdriver
import time


"""
Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
"""
link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Check value attribute checked for people_radio
    people_radio = browser.find_element_by_id("peopleRule")
    assert people_radio is not None, "People radio is not found"
    people_checked = people_radio.get_attribute("checked")
    print(f"Value of people radio: {people_checked}")
    assert people_checked == "true", "People radio is not selected by default"
    # Check status for robots_radio
    robots_radio = browser.find_element_by_id("robotsRule")
    assert robots_radio is not None, "Robot radio is not found"
    robots_status = robots_radio.get_attribute("checked")
    print(f"Value of robots radio: {robots_status}")
    assert robots_status == None, "Robots radio is selected by default"

finally:
    time.sleep(5)
    browser.quit()
