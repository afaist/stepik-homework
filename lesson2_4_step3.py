from selenium import webdriver

"""
Этот тест упадет с ошибкой, поскольку кнопка verify
появляется через секунду после загрузки страницы
"""
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    browser.quit()

