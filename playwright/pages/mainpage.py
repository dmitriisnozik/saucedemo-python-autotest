from playwright.sync_api import Page
from typing import Self

from pages.basepage import BasePage


class MainPage(BasePage):

    URL: str = 'https://www.saucedemo.com/inventory.html'
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.backpack_button = page.locator('button[data-test=add-to-cart-sauce-labs-backpack]')
        self.bike_light_button = page.locator('button[data-test=add-to-cart-sauce-labs-bike-light]')
        self.remove_backpack_button = page.locator('button[data-test=remove-sauce-labs-backpack]')
        self.remove_bike_light_button = page.locator('button[data-test=remove-sauce-labs-bike-light]')
        self.sort_container = page.locator('select[data-test=product_sort_container]')
        self.cart_indicator = page.locator('span.shopping_cart_badge')
        self.select_sort = page.locator('select[data-test=product_sort_container]')

    def load(self) -> Self:
        self.page.goto(self.URL)
        return self

    def add_backpack(self) -> Self:
        self.backpack_button.click()
        return self
    
    def add_bike_light(self) -> Self:
        self.bike_light_button.click()
        return self
    
    def remove_backpack(self) -> Self:
        self.remove_backpack_button.click()
        return self
    
    def remove_bike_light(self) -> Self:
        self.remove_bike_light_button.click()
        return self
    
    def get_cart_indicator(self) -> str:
        return self.cart_indicator.text_content()
    
    def sort_a_to_z(self) -> Self:
        self.select_sort.select_option(value='az')
        return self
    
    def sort_z_to_a(self) -> Self:
        self.select_sort.select_option(value='za')
        return self

    def sort_low_to_high(self) -> Self:
        self.select_sort.select_option(value='lohi')
        return self
    
    def sort_high_to_low(self) -> Self:
        self.select_sort.select_option(value='hilo')
        return self