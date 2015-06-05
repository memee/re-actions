Feature: Developer app authentication against API
  As a developer I want my app to be authenticated
  against API with provided api key, salt, signed key

  Scenario: Valid keys
    Given an app request has valid keys
    When the request was sent
    Then Http Unauthorized error should not be returned

  Scenario: Bad keys
    Given an app request has some bad key(s)
    When the request was sent
    Then Http Unauthorized error should be returned
