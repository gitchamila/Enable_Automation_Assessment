Feature: SauceDemo user journey

  Background:
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be redirected to the inventory page

  @working @cart @regression @positive
  Scenario: USER_JOURNEY_001_User can add a product to the cart
    Given the user is on the inventory page
    When the user opens the 'Sauce Labs Backpack' product and adds it to the cart
    Then the user can see 'Sauce Labs Backpack' in the cart with quantity 1

  @working @cart @regression @positive
  Scenario: USER_JOURNEY_002_User can remove a product from the cart
    Given the user is on the inventory page
    When the user opens the 'Sauce Labs Backpack' product and adds it to the cart
    Then the user can see 'Sauce Labs Backpack' in the cart with quantity 1
    When the user removes the product from the cart
    Then the user can continue shopping

  @working @cart @regression @positive
  Scenario: USER_JOURNEY_003_User can continue shopping and add another product to the cart
    Given the user is on the inventory page
    When the user opens the 'Sauce Labs Backpack' product and adds it to the cart
    Then the user can see 'Sauce Labs Backpack' in the cart with quantity 1
    When the user can continue shopping
    When the user opens the 'Sauce Labs Bike Light' product and adds it to the cart
    Then the user can see 'Sauce Labs Bike Light' in the cart with quantity 1
    And the user can checkout the product and fill the checkout information
    Then the user finished checkout process


