import pytest


@pytest.fixture(scope = "session")
def secondCheck():
    print("browser setup second check")
    return "pass"

@pytest.fixture(scope = "session")
def user_credentials(request):
    return request.param
