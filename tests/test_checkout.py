import pytest

from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
@pytest.mark.regression
def test_complete_purchase(login):

    products_page = ProductsPage(login)

    products_page.add_backpack_to_cart()
    products_page.click_cart()

    cart_page = CartPage(login)

    assert cart_page.is_backpack_displayed()

    cart_page.click_checkout()

    checkout_page = CheckoutPage(login)

    checkout_page.enter_customer_information(
        "Hari",
        "Test",
        "500001"
    )

    checkout_page.click_continue()
    checkout_page.click_finish()

    confirmation_message = checkout_page.get_confirmation_message()

    assert "Thank you for your order!" in confirmation_message