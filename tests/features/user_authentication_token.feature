Feature: Authentication of a end user
  As I developer I want to authenticate
  my end user and obtain a token for him

  Scenario: Valid credentials
    Given a request with a valid username/email and a password
    When the request was sent
    Then the response should contain a token
    And a token is valid

  Scenario: Invalid credentials
    Given a request with invalid username/email and password
    When the request was sent
    Then the response should have "400" status
