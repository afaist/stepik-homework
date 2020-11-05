import pytest


"""
Отметьте ниже только те тестовые методы, которые будут найдены и выполнены PyTest при запуске следующей команды:

pytest -v -m "smoke and not beta_users" test_task_run_1.py
"""

# Для выполнеия теста объявим browser fixture
@pytest.fixture
def browser():
    return 0

class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        print("\nNumber 1")
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        print("\nNumber 2")
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        print("\nNumber 3")
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        print("\nNumber 4")
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        print("\nNumber 5")
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        print("\nNumber 6")
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    print("\nNumber 7")
    assert True

