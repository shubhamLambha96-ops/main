from playwright.sync_api import Playwright


class ApiUtils:

    #login Api to gen Token
    def getToken(self, playwright: Playwright, userName, password):

        loginPayload = {"userEmail": userName, "userPassword": password}

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data=loginPayload,
                                            headers={
                                                "content-type": "application/json"
                                            })
        #assert response.ok
        response_Json = response.json()
        print(response_Json)

        return response_Json["token"]



    #create Order api call
    def createOrder(self, playwright:Playwright, userName, password):

        token = self.getToken(playwright, userName, password)
        print(token)
        orderPayload = {"orders": [{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}

        apiRequestContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response =  apiRequestContext.post("/api/ecom/order/create-order",
                                           data=orderPayload,
                                           headers={
                                               "authorization" : token,
                                               "content-type" : "application/json"
                                           })
        assert response.ok
        response_Json = response.json()
        print(response_Json)
        return response_Json["orders"][0]