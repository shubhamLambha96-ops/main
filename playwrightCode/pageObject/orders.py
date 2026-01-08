class Orders:

    def __init__(self, page):
        self.page = page


    def getOrderRow(self, orderId):
        row = self.page.locator("tr").filter(has_text=orderId)
        return row