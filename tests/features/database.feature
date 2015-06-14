Feature: Developer testing integration tests with database support
  As a developer I want database support for my tests with data rollback
  between tests

  Scenario: Verify name and value of a model object
    Given a single model object in the database
    When I open main index url
    Then I should single model as a JSON object

  Scenario: Verify session rollback
    Given a single model object in the database
    When I add a model object in this scenario
    Then I should have two model objects in the database

  Scenario: Verify session rollback p.2
    Given a single model object in the database
    When I make a query for that model object
    Then I should get an empty result
