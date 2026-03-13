from playwright.sync_api import Page


class CheckoutPage:
    PATH_STEP_ONE = "/checkout-step-one.html"
    PATH_STEP_TWO = "/checkout-step-two.html"
    PATH_COMPLETE = "/checkout-complete.html"

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("//button[@data-test='checkout']")
        self.continue_button = page.locator("//input[@data-test='continue']")
        self.finish_button = page.locator("//button[@data-test='finish']")

    def is_loaded_step_one(self) -> bool:
        return self.page.url.endswith(self.PATH_STEP_ONE)

    def is_loaded_step_two(self) -> bool:
        return self.page.url.endswith(self.PATH_STEP_TWO)

    def is_loaded_complete(self) -> bool:
        return self.page.url.endswith(self.PATH_COMPLETE)

    def checkout(self):
        self.checkout_button.click()

    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        self.page.locator("//input[@data-test='firstName']").fill(first_name)
        self.page.locator("//input[@data-test='lastName']").fill(last_name)
        self.page.locator("//input[@data-test='postalCode']").fill(postal_code)
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def has_checkout_complete_message(self) -> bool:
        return self.page.locator("//h2[@data-test='complete-header']", has_text="Thank you for your order!").is_visible()