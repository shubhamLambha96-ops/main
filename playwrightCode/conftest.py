import pytest


@pytest.fixture(scope = "session")
def secondCheck():
    print("browser setup second check")
    return "pass"

@pytest.fixture(scope = "session")
def user_credentials(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url", action="store", default="https://docs.pytest.org/en/stable/example/simple.html", help="url selection"
    )

@pytest.fixture
def browserInstance(playwright, request):

    browser = request.config.getoption("--browser_name")
    url = request.config.getoption("--url")
    print(url)

    if browser == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()
