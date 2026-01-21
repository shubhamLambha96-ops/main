Feature: test cases related to order transaction

  @k1
  Scenario Outline: order successfully placed and verify the order details

    Given place the order via api using <username> and <password>
    And the user is on landing page

    When I login to the portal with same <username> and <password>
    And navigate to order page and select the orderid details

    Then order message is successfully displayed

    Examples:
    | username                             |   password      |
    |  Shubhamlambha.1996@gmail.com        |   Shubh123      |
    | Suman@gmail.com                      |  Abcd@1234      |