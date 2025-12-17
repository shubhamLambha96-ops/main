import time

from playwright.sync_api import Playwright, Page, expect


def test_playwrightBasics(playwright : Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()

    #For the locators
    page.set_default_timeout(20000)

    #For the assertion
    expect.set_options(timeout=20000)

    page.goto("http://seleniumpractise.blogspot.com/2016/08/how-to-use-explicit-wait-in-selenium.html")
    page.get_by_text("Click me to start timer").click()
    expect(page.locator("//p[text()='WebDriver']")).to_be_visible()

    page.get_by_text("Blogger").click()
    expect(page.locator("//h2[text()='Publish your passions, your way']")).to_be_visible()
    time.sleep(5)