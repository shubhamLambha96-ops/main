import time
from playwright.sync_api import Page, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")
    time.sleep(5)

#single context headless chromium
def test_playwrightBasicsLocator(page : Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    time.sleep(5)
    page.click("#submit")
    expect(page.locator("//h1[text()='Logged In Successfully']")).to_have_text('Logged In Successfully')




