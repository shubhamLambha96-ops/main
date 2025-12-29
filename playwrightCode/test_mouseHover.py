import time

from playwright.sync_api import Page, expect


def test_MouseHover(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.locator("#mousehover").hover()
    time.sleep(5)
    page.get_by_role("link", name = "Top").click()