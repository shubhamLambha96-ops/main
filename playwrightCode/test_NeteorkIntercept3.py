import time

from playwright.sync_api import Playwright, expect
from playwrightCode.utils.apiBase import ApiUtils


def test_networkIntercept3(playwright: Playwright):

    #Get the token
    apiUtils = ApiUtils()
    token = apiUtils.getToken(playwright)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.add_init_script(f"""localStorage.setItem('token', '{token}')""")

    page.goto("https://rahulshettyacademy.com/client")
    time.sleep(5)
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()


