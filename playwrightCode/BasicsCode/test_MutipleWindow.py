import time

from playwright.sync_api import Playwright, Page, expect


def test_MultipleWindow(playwright : Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()

    page.goto("http://seleniumpractise.blogspot.com/2016/08/how-to-use-explicit-wait-in-selenium.html")

    with page.expect_popup() as newPage_info:
        page.get_by_text("Blogger").click()
        childPage = newPage_info.value

    expect(childPage.locator("//h2[text()='Publish your passions, your way']")).to_be_visible()

    page.bring_to_front()
    page.get_by_text("Click me to start timer").click()
    childPage.close()

    time.sleep(5)