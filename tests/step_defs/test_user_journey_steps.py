import os

from dotenv import load_dotenv
from pytest_bdd import given, parsers, scenarios, then, when

from pages.cart_page import CartPage
from pages.checkout import CheckoutPage
from pages.login_page import LoginPage
from pages.product_inventory_page import InventoryPage

load_dotenv()

scenarios("../features/login.feature")
scenarios("../features/user_journey.feature")


@given("the user is on the login page", target_fixture="login_page")
def navigate_to_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate(os.getenv("BASE_URL", "https://www.saucedemo.com"))
    return login_page


@when("the user enters valid credentials")
def login_with_valid_credentials(login_page):
    login_page.login(
        os.getenv("SAUCE_USERNAME", "standard_user"),
        os.getenv("SAUCE_PASSWORD", "secret_sauce"),
    )


@then("the user should be redirected to the inventory page")
def verify_inventory_page(page):
    page.wait_for_url("**/inventory.html")
    assert page.url.endswith("/inventory.html"), (
        f"Expected inventory page, got {page.url}"
    )


@given("the user is on the inventory page", target_fixture="inventory")
def verify_on_inventory_page(page):
    inventory = InventoryPage(page)
    assert inventory.is_loaded(), "Inventory page did not load"
    return inventory


@when( parsers.parse( "the user opens the '{product_name}' product and adds it to the cart" ))
def open_product_and_add_to_cart(page, product_name):
    inventory = InventoryPage(page)
    inventory.open_product_by_name(product_name)
    inventory.add_to_cart()


@then(  parsers.parse( "the user can see '{product_name}' in the cart with quantity {quantity:d}" ))
def verify_product_in_cart(page, product_name, quantity):
    cart = CartPage(page)
    cart.go_to_cart()
    assert cart.is_loaded(), "Cart page did not load"
    assert cart.has_product(product_name), (  f"'{product_name}' should be visible in the cart" )
    assert cart.get_product_quantity(product_name) == quantity, ( f"'{product_name}' quantity should be {quantity}")


@when("the user removes the product from the cart")
def remove_product_from_cart(page):
    cart = CartPage(page)
    cart.remove_product_from_cart()


@when("the user can continue shopping")
@then("the user can continue shopping")
def continue_shopping(page):
    cart = CartPage(page)
    cart.continue_shopping()


@then("the user can checkout the product and fill the checkout information")
def checkout_product(page):
    checkout = CheckoutPage(page)
    checkout.checkout()
    assert checkout.is_loaded_step_one(), ( f"Expected checkout page, got {page.url}" )
    checkout.fill_checkout_information(  first_name="Chamila", last_name="Rosedale", postal_code="06320" ) 
    assert checkout.is_loaded_step_two(), ( f"Expected checkout page, got {page.url}" )


@then("the user finished checkout process")
def finished_checkout_process(page):
    checkout = CheckoutPage(page)
    checkout.finish_checkout()
    assert checkout.is_loaded_complete(), (f"Expected checkout complete page, got {page.url}" )
    assert checkout.has_checkout_complete_message(), (f"Expected checkout complete message, got {page.url}")
