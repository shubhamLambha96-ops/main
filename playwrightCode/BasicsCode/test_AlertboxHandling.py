import time

from playwright.sync_api import Page


def test_AlertboxWithOkButton(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.on("dialog", lambda dialog : dialog.accept())
    page.locator("#alertbtn").click()

    time.sleep(5)

    page.locator("#alertbtn").click()
    time.sleep(5)


def test_AlertboxWithOkAndCancelButton(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    should_accept = True

    def handel_dialog(dialog):
        if should_accept:
            dialog.accept()
        else:
            dialog.dismiss()

    page.on("dialog", handel_dialog)

    page.locator("#confirmbtn").click()
    time.sleep(5)

    should_accept = False
    page.locator("#confirmbtn").click()







