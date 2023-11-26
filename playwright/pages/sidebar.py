from playwright.sync_api import Page
from typing import Self


class SideBar:
    def __init__(self, page: Page):
        self.page = page
        self.close_button = page.locator('button[id=react-burger-cross-btn]')
        self.all_items_button = page.locator('a[id=inventory_sidebar_link]')
        self.about_button = page.locator('a[id=about_sidebar_link]')
        self.logout_button = page.locator('a[id=logout_sidebar_link]')
        self.reset_app_state_button = page.locator('a[id=reset_sidebar_link]')

    def reset_app_state(self) -> Self:
        self.reset_app_state_button.click()
        return self
    
    def close_sidebar(self):
        self.close_button.click()
        from pages.mainpage import MainPage
        return MainPage(self.page)
    
    def logout(self):
        self.logout_button.click()
        from pages.loginpage import LoginPage
        return LoginPage(self.page)
    
    def about(self) -> Self:
        self.about_button.click()
        return self
    