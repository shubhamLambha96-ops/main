import os
import pytest
import allure
from allure_commons.types import AttachmentType


def pytest_configure(config):
    """
    Runs once in the MASTER process only (xdist-safe)
    """
    if not hasattr(config, "workerinput"):  # master node
        base_dir = os.path.dirname(os.path.abspath(__file__))
        results_dir = os.path.join(base_dir, "test-results")

        os.makedirs(results_dir, exist_ok=True)
        os.makedirs(os.path.join(results_dir, "screenshots"), exist_ok=True)
        os.makedirs(os.path.join(results_dir, "traces"), exist_ok=True)


@pytest.fixture(scope="session")
def secondCheck():
    print("browser setup second check")
    return "pass"


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://docs.pytest.org/en/stable/example/simple.html",
        help="url selection",
    )


@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    url = request.config.getoption("--url")
    print(url)

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError("Unsupported browser")

    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attach screenshot to Allure report when a test fails.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("browserInstance")
        if page:
            allure.attach(
                page.screenshot(),
                name="Screenshot on failure",
                attachment_type=AttachmentType.PNG,
            )
