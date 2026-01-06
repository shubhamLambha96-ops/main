import time

from playwright.sync_api import Playwright

fakeOrderResponse = {"data":[],"message":"No Orders"}

def response_intercept(route):
    route.fulfill(
        json = fakeOrderResponse
    )


def test_networkIntercept(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Mock the data
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", response_intercept)

    page.goto("https://rahulshettyacademy.com/client")

    page.locator("#userEmail").fill("Shubhamlambha.1996@gmail.com")
    page.locator("#userPassword").fill("Shubh123")
    page.locator("#login").click()

    page.get_by_role("button", name="ORDERS").click()
    time.sleep(5)
    text = page.locator(".mt-4").text_content()
    print(text)
    assert text == " You have No Orders to show at this time. Please Visit Back Us "