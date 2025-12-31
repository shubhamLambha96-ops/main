from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"item-4-img-link\"]")).to_be_visible()
    #soome assertion

    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()

    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"continue-shopping\"]")).to_be_visible()

    page.locator("[data-test=\"checkout\"]").click()
    expect(page.locator("[data-test=\"cancel\"]")).to_be_visible()

    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("shubham")
    page.locator("[data-test=\"firstName\"]").press("Tab")
    page.locator("[data-test=\"lastName\"]").fill("lambha")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("110000")
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"item-4-title-link\"]")).to_be_visible()

    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"pony-express\"]")).to_be_visible()

    page.locator("[data-test=\"back-to-products\"]").click()

    # ---------------------
    context.close()
    browser.close()
