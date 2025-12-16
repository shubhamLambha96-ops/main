import pytest


@pytest.fixture(scope = "session")
def secondCheck():
    print("browser setup second check")
    return "pass"