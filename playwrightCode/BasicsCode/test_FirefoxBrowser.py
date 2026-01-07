import time

from playwright.sync_api import Playwright, Page, expect


def test_playwrightBasics(playwright : Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("http://seleniumpractise.blogspot.com/2016/08/how-to-use-explicit-wait-in-selenium.html")

    with page.expect_popup() as newPage_info:
        page.get_by_text("Blogger").click()
        childPage = newPage_info.value

    expect(childPage.locator("//p[text()='Create a unique and beautiful blog easily.']")).to_be_visible(timeout=20000)
    #childPage.close()
    page.bring_to_front()

    time.sleep(2)
