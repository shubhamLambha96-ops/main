import time


def test_playwrightBasics(playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.google.com")
    time.sleep(5)