Feature: Developer testing integration tests with Travis
  As a developer I want a simple integration test
  to pass on Travis

  Scenario: Verify name and value of a model object
    Given initializedb script populate data
    When I open main index url
    Then I should single model as a JSON object
