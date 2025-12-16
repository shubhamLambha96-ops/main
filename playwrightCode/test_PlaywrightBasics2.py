import time
from playwright.sync_api import Page, expect

def test_playwrightBasicsLocator3(page : Page):
    page.goto("https://practicetestautomation.com/practice-test-table/")

    #drop down
    page.get_by_role("combobox").select_option("col_lang")

    #radio
    page.get_by_role("radio", name="Java").check()

    #checkbox
    page.get_by_role("checkbox", name="Beginner").uncheck()
    page.get_by_role("checkbox", name="Beginner").check()

    #heading h1
    text = page.get_by_role("heading").first.text_content()
    print(text)

    #other heading
    #h2_locator = page.locator("h2").first
    #h2_locator = page.locator("h2").last
    h2_locator= page.locator("h2").nth(0)
    h2_locator.wait_for(state="visible")  # waits until the h2 is visible
    text = h2_locator.text_content()
    print(text)


    #other option
    h2_locator1 = page.locator("h2").filter(has_text="Automation Courses").text_content()
    #h2_locator1.wait_for(state="visible")  # ensure it’s visible
    #text2 = h2_locator1.text_content()
    print(h2_locator1)

    page.get_by_role("link", name="XPath Locators for Selenium").click()
    time.sleep(5)