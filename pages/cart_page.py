from playwright.sync_api import Page


class CartPage:
    PATH = "/cart.html"

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator('[data-test="inventory-item"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.cart_link = page.locator('//a[@data-test="shopping-cart-link"]')
        self.remove_button = self.page.locator("//button[@data-test='remove-sauce-labs-backpack']")

    def is_loaded(self) -> bool:
        return self.page.url.endswith(self.PATH)

    def go_to_cart(self):
        self.cart_link.click()

    def has_product(self, name: str) -> bool:
        return self.page.locator('[data-test="inventory-item-name"]', has_text=name).is_visible()

    def get_product_quantity(self, name: str) -> int:
        item = self.cart_items.filter(
            has=self.page.locator('[data-test="inventory-item-name"]', has_text=name)
        )
        return int(item.locator('[data-test="item-quantity"]').text_content())

    def remove_product_from_cart(self):
        self.remove_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()
