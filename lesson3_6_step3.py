import time
import math
from selenium import webdriver
import pytest
import pyperclip


"""
открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с
"Correct!"
В упавших тестах найдите кусочки послания. Тест должен падать, если текст в
опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки текста
в одно предложение и отправьте в качестве ответа на это задание.


Запускать командой:
    pytest -s --tb=no lesson3_6_step3.py
"""
# Создадим глобальную переменную для ответа
# ответ будет в буфере обмена и на экране
lesson_answer = ""

@pytest.fixture(scope="session", autouse=True)
def print_lesson():
    """
    Фикстура для печати ответа
    и копирования ответа в буфер обмена
    """
    global lesson_answer
    yield
    # Это будет выполняться после прохождения всех тестов
    print("\nЭто ответ --->>> ",lesson_answer)
    pyperclip.copy(lesson_answer) # Ответ на вопрос в буфере обмена
    print("Ответ также скопирован в буфер обмена!")

@pytest.fixture(scope="function")
def browser():
    """
    Открываем и закрываем браузер для каждого теста
    """
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    browser.quit()


# Список ссылок, в задании указано, что передавать нужно именно
# список ссылок
parametrs = ["https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('links', parametrs)
def test_links(browser,  links):
    global lesson_answer
    browser.get(links)
    text = work(browser)
    if text == "Correct!":
        assert True
    else:
        lesson_answer += text
        assert False


def work(browser):
    result = ""
    try:
        txt = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        txt.send_keys(str(answer))
        btn = browser.find_element_by_class_name("submit-submission")
        btn.click()
        hint = browser.find_element_by_class_name("smart-hints__hint")
        result = hint.text

    except Exception as e:
        print(type(e))
        print(e.args)
        print(e)

    finally:
        return result

