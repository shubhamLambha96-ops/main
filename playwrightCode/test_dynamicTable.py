import time

from playwright.sync_api import Page, expect


def test_MouseActivityMethod(page : Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    priceColValue = None

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceColValue = index
            print(f"Price column value is {priceColValue}")
            break

    assert priceColValue is not None

    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")




