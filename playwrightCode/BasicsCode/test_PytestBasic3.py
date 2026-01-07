import pytest


@pytest.fixture(scope = "function")
def initialCheck2():
    print("browser setup")
    yield
    print("browser teardown")


def test_login3(initialCheck2):
    print("Test 3 execution started")
