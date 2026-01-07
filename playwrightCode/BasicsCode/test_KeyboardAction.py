import time

from playwright.sync_api import Page, expect


def test_MouseHover(page : Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").click()
    page.keyboard.type("playwright")

    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")

    page.keyboard.type("standard_user")
    page.keyboard.press("Tab")

    page.keyboard.type("secret_sauce")

    page.keyboard.press("Enter")