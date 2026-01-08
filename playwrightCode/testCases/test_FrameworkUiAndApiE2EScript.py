import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from playwrightCode.pageObject.dashboard import Dashboard
from playwrightCode.pageObject.login import LoginPage
from playwrightCode.pageObject.orders import Orders

from playwrightCode.utils.apiBase import ApiUtils

with open('playwrightCode/data/userCredentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials' , user_credentials_list)
def test_FrameworkPlaywrightBasics(playwright : Playwright, user_credentials):

    userName = user_credentials['userName']
    password = user_credentials['password']

    #API Call to get order id
    apiUtils = ApiUtils()
    orderId = apiUtils.createOrder(playwright, userName, password)
    print(orderId)

    #Ui
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")

    #Login page
    loginPage = LoginPage(page)
    loginPage.login(userName, password)

    #dashboard
    dashboardPage = Dashboard(page)
    dashboardPage.clickOnAllOrdersLink()

    #OrderDetails Page
    Order = Orders(page)
    row = Order.getOrderRow(orderId)

    expect(row).to_be_visible()
    page.close()

