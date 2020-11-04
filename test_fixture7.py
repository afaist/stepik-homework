import pytest


"""
У нас есть набор тестов, который использует несколько фикстур. Посчитайте,
сколько смайликов будет напечатано при выполнении этого тестового класса?
"""


@pytest.fixture(scope="class") # Будет вызвана один раз для класса
def prepare_faces():
    print()
    print("^_^", "\n")
    yield
    print()
    print(":3", "\n")


@pytest.fixture() # Будет вызвана при передаче в качестве параметра
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True) # Будет вызвана для каждого теста
def print_smiling_faces():
    print()
    print(":-P", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        #
        print("First test")

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        #
        print("Second test")

