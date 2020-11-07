link = "http://selenium1py.pythonanywhere.com/"


"""
Запускать тест либо:
    pytest -s -v --browser_name=chrome test_parser.py
либо:
    pytest -s -v --browser_name=firefox test_parser.py
"""
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

