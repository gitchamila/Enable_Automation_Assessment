from playwright.sync_api import Page


class InventoryPage:
    PATH = "/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator('[data-test="inventory-item"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.add_to_cart_button = page.locator("//button[@data-test='add-to-cart']")

    def is_loaded(self) -> bool:
        return self.page.url.endswith(self.PATH)

    def open_product_by_name(self, name: str):
        self.page.locator('[data-test="inventory-item-name"]', has_text=name).click()

    def add_to_cart(self):
        self.add_to_cart_button.click()
