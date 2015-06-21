Feature: User registration
  As a developer I want to register some user
  with a request to the API and obtain valid token

  Scenario: Valid data input
    Given registration data
      | username | first_name | last_name | email   |
      | user1    | John       | Kovac     | m@m.com |
      | m@m.com  | John       | Kovac     | m@m.com |
      | m@m.com  |            |           | m@m.com |
    When I post it to user registration url
    Then I get a user token in a response

  Scenario: Invalid data input
    Given registration data
      | username | first_name | last_name | email   |
      | --!@     | John       | Kovac     | m@m.com |
      | user1    | John       | Kovac     | none    |
      | !!       | John       | Kovac     | some    |
      |          | John       | Kovac     | m@m.com |
      | a@a.com  | John       | Kovac     | m@m.com |
    When I post it to user registration url
    Then I should get a "incomplete data" warning with a "400" status
