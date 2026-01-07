import pytest


@pytest.fixture(scope = "function")
def initialCheck():
    print("browser setup")
    return "shubham"


def test_firstTest(initialCheck):
    print("This is the first test")
    print(initialCheck)
    assert initialCheck == "shubham"

@pytest.mark.smoke
def test_secondTest(initialCheck):
    print("This is the second test")
    print(initialCheck)

def test_secondTest2(initialCheck):
    print("This is the second2 test")
    print(initialCheck)

@pytest.mark.smoke
def test_secondTest3(initialCheck):
    print("This is the second3 test")
    print(initialCheck)

