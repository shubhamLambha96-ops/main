import time
from playwright.sync_api import Playwright, expect

from playwrightCode.utils.apiBase import ApiUtils


def test_playwrightBasics(playwright : Playwright):

    #API Call to get order id
    apiUtils = ApiUtils()
    orderId = apiUtils.createOrder(playwright)
    print(orderId)

    #Ui
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")

    page.locator("#userEmail").fill("Shubhamlambha.1996@gmail.com")
    page.locator("#userPassword").fill("Shubh123")
    page.locator("#login").click()

    page.get_by_role("button", name="ORDERS").click()

    row = page.locator("tr").filter(has_text=orderId)
    expect(row).to_be_visible()
    time.sleep(5)

