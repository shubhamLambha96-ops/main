
def test_new1(page):
    page.goto("https://rahulshettyacademy.com/client")
    page.screenshot(path="after_login.png", full_page=True)
