def test_login(page):
    page.goto("https://www.google.com")
    print(page.title())


def test_login1(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    print(page.title())
    page.fill('#username','student')
    page.fill('#password','Password123')
    page.click('#submit')


def test_login2(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    print(page.title())
    page.fill("[name='username']",'student')
    page.fill("[name='password']", 'Password123')
    page.click('#submit')


def test_login3(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    print(page.title())
    page.fill("//input[@id='username']", 'student')
    page.fill("//input[@name='password']", 'Password123')
    page.click("//button[@id='submit']")

