import time

from playwright.sync_api import Playwright


def response_intercept(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/695cdce3c941646b7a821786")


def test_networkIntercept2(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Mock the data
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", response_intercept)

    page.goto("https://rahulshettyacademy.com/client")

    page.locator("#userEmail").fill("Shubhamlambha.1996@gmail.com")
    page.locator("#userPassword").fill("Shubh123")
    page.locator("#login").click()

    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name= "View").first.click()
    time.sleep(5)

    text = page.locator("//p[@class='blink_me']").text_content()
    print(text)