import json
from pathlib import Path

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

        BASE_DIR = Path(__file__).resolve().parents[1]
        DATA_FILE = BASE_DIR / "payloads" / "orderApiPayload.json"

        with open(DATA_FILE) as f:
            orderPayload = json.load(f)

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