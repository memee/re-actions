Feature: Authentication of a user request
  As I developer I want to authenticate
  every request invoked by my app end user

  Scenario Outline: Requests authentication
    Given a request from {someuser} for any url
    And the request has {sometoken} in the header
    When the request was sent
    Then the request is {authenticated}
    And the response has "{somestatus}"

  Examples:
    | someuser     | sometoken  | authenticated  | somestatus  |
    | registered   | valid      | yes            | 20*         |
    | registered   | invalid    | no             | 401         |
    | unregistered | invalid    | no             | 401         |
    | unregistered | stolen     | no             | 401         |
    | registered   | stolen     | no             | 401         |
