import pytest

from pages.loginpage import LoginPage
from pages.mainpage import MainPage
from pages.cartpage import CartPage
from playwright.sync_api import Page


@pytest.fixture
def login_page(page:Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def main_page(page:Page) -> MainPage:
    return MainPage(page)

@pytest.fixture
def cart_page(page:Page) -> CartPage:
    return CartPage(page)
