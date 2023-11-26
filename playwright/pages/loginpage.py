from playwright.sync_api import Page
from typing import Self

from pages.mainpage import MainPage


class LoginPage:

    URL: str = 'https://saucedemo.com'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_field = page.locator('input[data-test=username]')
        self.password_field = page.locator('input[data-test=password]')
        self.submit_button = page.locator('input[data-test=login-button]')
        self.error = page.locator('h3[data-test=error]')

    def load(self) -> Self:
        self.page.goto(self.URL)
        return self

    def sign_in(self, username: str, password: str) -> MainPage | Self:
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.submit_button.click()
        if self.page.query_selector('input[data-test=username]') is None:
            return MainPage(self.page)
        return self
    
    def get_error_message(self) -> str:
        return self.error.text_content()
