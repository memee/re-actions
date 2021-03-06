Feature: Developer app registration
  As a developer I want to register my app
  and obtain APIKey with SecretKey

  Scenario: Valid data input
    Given app registration data
      | app_name | first_name | last_name | email   |
      | app1     | John       | Kovac     | m@m.com |
    When I post it to the app registration url
    Then I get an APIKey and a SecretKey in a response

  Scenario: Incomplete data input
    Given app registration data
      | app_name | first_name | last_name | email   |
      |          | John       | Kovac     | m@m.com |
      | app1     | John       | Kovac     |         |
    When I post it to the app registration url
    Then I should get a warning with a "400" status

  Scenario: Invalid data input
    Given app registration data
      | app_name | first_name | last_name | email   |
      | --!@     | John       | Kovac     | m@m.com |
      | app1     | John       | Kovac     | none    |
      | !!       | John       | Kovac     | some    |
    When I post it to the app registration url
    Then I should get a warning with a "400" status
