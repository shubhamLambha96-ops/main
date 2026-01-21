import pytest
from playwright.sync_api import expect
from pytest_bdd import given, when, then, scenarios, parsers

from playwrightCode.pageObject.dashboard import Dashboard
from playwrightCode.pageObject.login import LoginPage
from playwrightCode.pageObject.orders import Orders
from playwrightCode.utils.apiBase import ApiUtils

scenarios("orderTransaction.feature")

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the order via api using {username} and {password}'))
def placeOrder(playwright, username, password, shared_data):
    # API Call to get order id
    apiUtils = ApiUtils()
    orderId = apiUtils.createOrder(playwright, username, password)
    print(orderId)
    shared_data['orderId'] = orderId

@given('the user is on landing page')
def userIsOnLandingPage(browserInstance, shared_data):
    # Ui
    page = browserInstance
    page.goto("https://rahulshettyacademy.com/client")
    shared_data['page'] = page

@when(parsers.parse('I login to the portal with same {username} and {password}'))
def loginToPortal(shared_data, username, password):
    page = shared_data['page']
    # Login page
    loginPage = LoginPage(page)
    loginPage.login(username, password)

@when('navigate to order page and select the orderid details')
def orderDetailsPage(shared_data):
    page = shared_data['page']
    # dashboard
    dashboardPage = Dashboard(page)
    dashboardPage.clickOnAllOrdersLink()

    # OrderDetails Page
    orderId = shared_data['orderId']
    Order = Orders(page)
    row = Order.getOrderRow(orderId)
    shared_data['row'] = row

@then('order message is successfully displayed')
def orderMessagesPage(shared_data):
    row = shared_data['row']
    expect(row).to_be_visible()