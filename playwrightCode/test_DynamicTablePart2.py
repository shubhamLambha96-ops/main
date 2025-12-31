import time

from playwright.sync_api import Page, expect


def test_MouseActivityMethod(page : Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    header = page.locator("th").all_inner_texts()
    #header =["Veg/fruit name", "Price", "Discount price"]

    priceColumnIndex = header.index("Price")

    riceRow = page.locator("tr").filter(has_text="Rice")
    # Rice | 37 | 46

    expect(riceRow.locator("td").nth(priceColumnIndex)).to_have_text("37")

