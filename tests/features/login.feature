Feature: SauceDemo user journey

  @working @login @regression @positive
  Scenario: LOGIN_001_Login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be redirected to the inventory page
