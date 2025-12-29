import time

from playwright.sync_api import Page, expect


def test_MouseActivityMethod(page : Page):
    page.goto("https://demoqa.com/buttons")

    #doubleClick
    double_click_btn = page.locator("#doubleClickBtn")
    double_click_btn.dblclick()

    expect(page.locator("#doubleClickMessage")).to_have_text("You have done a double click")

    time.sleep(5)

    #right Click
    right_Click_btn = page.locator("#rightClickBtn")
    right_Click_btn.click(button="right")
    expect(page.locator("#rightClickMessage")).to_have_text("You have done a right click")

    time.sleep(5)

    #single click
    page.get_by_role("button", name="Click Me", exact = True).click()
    expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")

    time.sleep(5)
