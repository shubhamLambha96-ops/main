import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from playwrightCode.utils.apiBase import ApiUtils

with open('playwrightCode/data/userCredentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials' , user_credentials_list)
def test_FrameworkPlaywrightBasics(playwright : Playwright, user_credentials):

    #API Call to get order id
    apiUtils = ApiUtils()
    orderId = apiUtils.createOrder(playwright)
    print(orderId)

    #Ui
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")

    #Login page
    page.locator("#userEmail").fill(user_credentials['userName'])
    page.locator("#userPassword").fill(user_credentials['password'])
    page.locator("#login").click()

    #dashboard
    page.get_by_role("button", name="ORDERS").click()

    #OrderDetails Page
    row = page.locator("tr").filter(has_text=orderId)
    expect(row).to_be_visible()
    time.sleep(5)

