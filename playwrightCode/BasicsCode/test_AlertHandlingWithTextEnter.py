import time

from playwright.sync_api import Page, expect


def test_AlertboxWithTextEnter(page : Page):
    page.goto("https://demoqa.com/alerts")

    def handel_Dialog(dialog):
        dialog.accept("Shubham Kumar")

    page.on("dialog", handel_Dialog)

    page.locator("#promtButton").click()

    expect (page.locator("//span[text()='Shubham Kumar']")).to_be_visible()
    time.sleep(5)



def test_AlertboxWithGetText(page : Page):
    page.goto("https://demoqa.com/alerts")

    alert_text = ""

    def handel_Dialog(dialog):
        nonlocal alert_text
        alert_text = dialog.message
        print(alert_text)
        dialog.accept()

    page.on("dialog", handel_Dialog)

    page.locator("#alertButton").click()
    time.sleep(5)
