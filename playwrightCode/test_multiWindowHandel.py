import time

from playwright.sync_api import Playwright, Page, expect


def test_MultipleWindow(playwright : Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    context = firefoxBrowser.new_context()
    context1 = firefoxBrowser.new_context()
    page = context.new_page()

    page.goto("https://www.hdfc.bank.in/")

    with page.expect_popup() as personalLoanPage_info:
        page.locator("//a[text()='Personal Loan']").click()
        personalLoanPage = personalLoanPage_info.value

    with page.expect_popup() as carLoanPage_info:
        page.locator("//a[text()='Car Loan']").click()
        carLoanPage = carLoanPage_info.value

    with page.expect_popup() as businessLoanPage_info:
        page.locator("//a[text()='Business Loan']").click()
        businessLoanPage = businessLoanPage_info.value

    time.sleep(5)

    carLoanPage.bring_to_front()
    expect(carLoanPage).to_have_title("Car Loan Online - Apply New Car Loan & Get up to 100% Funding | HDFC Bank")
    time.sleep(5)

    personalLoanPage.bring_to_front()
    expect(personalLoanPage).to_have_title("Get Instant Personal Loan Online Starting 9.99% | HDFC Bank")
    time.sleep(5)

    businessLoanPage.bring_to_front()
    expect(businessLoanPage).to_have_title("Apply for Business Loan Online at Lowest Interest Rate | HDFC Bank")
    time.sleep(5)

    all_pages = context.pages

    for p in all_pages:
        print(p.title())
        print(p.url)

    secondPage = context1.new_page()
    secondPage.goto("https://www.google.com/")
    time.sleep(5)
    secondPage.close()
    time.sleep(5)



