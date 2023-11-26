from playwright.sync_api import Page
from typing import Self


class CartPage:

    URL: str = 'https://www.saucedemo.com/cart.html'

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator('button[data-test=checkout]')
        self.continue_shopping_button = page.locator('button[data-test=continue-shopping]')
        self.checkout_name_field = page.locator('input[data-test=firstName]')
        self.checkout_last_name_field = page.locator('input[data-test=lastName]')
        self.checkout_zipcode_field = page.locator('input[data-test=postalCode]')
        self.checkout_continue_button = page.locator('input[data-test=continue]')
        self.checkout_cancel_button = page.locator('button[data-test=cancel]')
        self.checkout2_finish_button = page.locator('button[data-test=finish]')
        self.checkout2_cancel_button = page.locator('button[data-test=cancel]')
        self.subtotal = page.locator('div.summary_subtotal_label')
        self.tax = page.locator('div.summary_tax_label')
        self.total = page.locator('div.summary_info_label.summary_total_label')

    def load(self) -> Self:
        self.page.goto(self.URL)
        return self

    def checkout(self) -> Self:
        self.checkout_button.click()
        return self
    
    def checkout_continue(self, first_name: str, last_name: str, zip: str) -> Self:
        self.checkout_name_field.fill(first_name)
        self.checkout_last_name_field.fill(last_name)
        self.checkout_zipcode_field.fill(zip)
        self.checkout_continue_button.click()
        return self

    def checkout_cancel(self) -> Self:
        self.checkout_cancel_button.click()
        return self
    
    def checkout_finish(self) -> Self:
        self.checkout2_finish_button.click()
        return self
    
    def get_final_title(self) -> str:
        if (title := self.page.locator('span.title')) is not None:
            return title.text_content()
        return None

    def get_total_prices(self) -> dict:
        return {
            'subtotal': float(self.subtotal.text_content().split('$')[1]),
            'tax': float(self.tax.text_content().split('$')[1]),
            'total': float(self.total.text_content().split('$')[1]),
        }
