from playwright.sync_api import Page

from pages.sidebar import SideBar


class BasePage:
    
    def __init__(self, page: Page) -> None:
        self.page = page
        self.sidebar_button = page.locator('button[id=react-burger-menu-btn]')
        self.cart_button = page.locator('a[class=shopping_cart_link]')

    def open_sidebar(self) -> SideBar:
        self.sidebar_button.click()
        return SideBar(self.page)
    
    def open_cart(self):
        self.cart_button.click()
        from pages.cartpage import CartPage
        return CartPage(self.page)
