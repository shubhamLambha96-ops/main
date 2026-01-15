import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from playwrightCode.pageObject.dashboard import Dashboard
from playwrightCode.pageObject.login import LoginPage
from playwrightCode.pageObject.orders import Orders

from playwrightCode.utils.apiBase import ApiUtils
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "userCredentials.json"

with open(DATA_FILE) as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials' , user_credentials_list)
def test_FrameworkPlaywrightBasics(playwright : Playwright, browserInstance, user_credentials):

    userName = user_credentials['userName']
    password = user_credentials['password']

    #API Call to get order id
    apiUtils = ApiUtils()
    orderId = apiUtils.createOrder(playwright, userName, password)
    print(orderId)

    #Ui
    page = browserInstance
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

