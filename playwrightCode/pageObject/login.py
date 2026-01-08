class LoginPage:

    def __init__(self, page):
        self.page = page


    def login(self, userName, password):
        self.page.locator("#userEmail").fill(userName)
        self.page.locator("#userPassword").fill(password)
        self.page.locator("#login").click()