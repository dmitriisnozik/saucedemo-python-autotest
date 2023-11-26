import configparser
from playwright.sync_api import Page
from faker import Faker
from pytest import approx

from pages.loginpage import LoginPage


config = configparser.ConfigParser()
config.read('settings.ini')

username = config['default']['username']
password = config['default']['password']

fake = Faker()


def test_e2e_positive(
    page: Page,
    login_page: LoginPage,
) -> None:

    result = login_page.load().sign_in(
        username,
        password
    ).add_backpack().add_bike_light().remove_backpack().open_cart(
    ).checkout().checkout_continue(
        fake.first_name(),
        fake.last_name(),
        fake.zipcode(),
    ).checkout_finish()

    assert result.get_final_title() == 'Checkout: Complete!'


def test_tax_calculation(
        page: Page,
        login_page: LoginPage,
) -> None:
    
    result = login_page.load().sign_in(
        username,
        password
    ).add_bike_light().open_cart(
    ).checkout().checkout_continue(
        fake.first_name(),
        fake.last_name(),
        fake.zipcode(),
    ).get_total_prices()

    assert round(result['subtotal']/12.4875, 2) == approx(result['tax'])


    result = login_page.load().sign_in(
        username,
        password
    ).add_backpack().open_cart(
    ).checkout().checkout_continue(
        fake.first_name(),
        fake.last_name(),
        fake.zipcode(),
    ).get_total_prices()

    assert round(result['subtotal']/12.4875, 2) == approx(result['tax'])


def test_cart_indicator(
        page: Page,
        login_page: LoginPage,
) -> None:
    
    result = login_page.load().sign_in(
        username,
        password
    )
    
    assert result.add_backpack().get_cart_indicator() == '1'
    assert result.add_bike_light().get_cart_indicator() == '2'
    assert result.remove_backpack().get_cart_indicator() == '1'


def test_reset_app_state(
        page: Page,
        login_page: LoginPage,
) -> None:
    
    result = login_page.load().sign_in(
        username,
        password
    ).add_bike_light()

    assert result.get_cart_indicator() == '1'

    result.open_sidebar().reset_app_state().close_sidebar().add_backpack()

    assert result.get_cart_indicator() == '1'


def test_logout(
        page: Page,
        login_page: LoginPage,
) -> None:
    
    result = login_page.load().sign_in(
        username,
        password
    )

    assert result.page.query_selector('input[data-test=login-button]') is None

    result.open_sidebar().logout()

    assert result.page.query_selector('input[data-test=login-button]') is not None

def test_about(
        page: Page,
        login_page: LoginPage,
) -> None:
    
    result = login_page.load().sign_in(
        username,
        password
    ).open_sidebar().about()

    assert result.page.url == 'https://saucelabs.com/'

def test_sort(
        page: Page,
        login_page: LoginPage,
) -> None:
    result = login_page.load().sign_in(
        username,
        password
    )

    assert result.sort_z_to_a().page.locator(
        'div.inventory_list > div:nth-child(1) > .inventory_item_description > .inventory_item_label > a > .inventory_item_name'
    ).text_content() == 'Test.allTheThings() T-Shirt (Red)' 

    assert result.sort_a_to_z().page.locator(
        'div.inventory_list > div:nth-child(1) > .inventory_item_description > .inventory_item_label > a > .inventory_item_name'
    ).text_content() == 'Sauce Labs Backpack' 

    assert result.sort_low_to_high().page.locator(
        'div.inventory_list > div:nth-child(1) > .inventory_item_description > .inventory_item_label > a > .inventory_item_name'
    ).text_content() == 'Sauce Labs Onesie' 

    assert result.sort_high_to_low().page.locator(
        'div.inventory_list > div:nth-child(1) > .inventory_item_description > .inventory_item_label > a > .inventory_item_name'
    ).text_content() == 'Sauce Labs Fleece Jacket' 