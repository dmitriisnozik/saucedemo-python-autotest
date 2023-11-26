import configparser
from playwright.sync_api import Page
from faker import Faker

from pages.loginpage import LoginPage
from pages.mainpage import MainPage
from pages.cartpage import CartPage


config = configparser.ConfigParser()
config.read('settings.ini')


fake = Faker()


def test_e2e_positive(
    page: Page,
    login_page: LoginPage,
) -> None:

    result = login_page.load().sign_in(
        fake.user_name(),
        fake.password()
    )

    assert 'Username and password do not match any user' in result.get_error_message()

def test_locked_out_user(
        page: Page,
        login_page: LoginPage,
) -> None:
    
    result = login_page.load().sign_in(
        config['locked']['username'],
        config['locked']['password']
    )

    assert 'user has been locked out' in result.get_error_message()

def test_unauthorized_main_page(
        page: Page,
        main_page: MainPage
) -> None:
    
    result = main_page.load()

    assert "You can only access '/inventory.html' when you are logged in" in result.page.locator('h3[data-test=error]').text_content()

def test_unauthorized_cart_page(
        page: Page,
        cart_page: CartPage
) -> None:
    
    result = cart_page.load()

    assert "You can only access '/cart.html' when you are logged in" in result.page.locator('h3[data-test=error]').text_content()

