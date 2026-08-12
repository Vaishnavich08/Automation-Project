import pytest

from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.mark.smoke
@pytest.mark.regression
def test_add_product_to_cart(login):

    products_page = ProductsPage(login)

    assert products_page.is_products_page_displayed()

    products_page.add_backpack_to_cart()
    products_page.click_cart()

    cart_page = CartPage(login)

    assert cart_page.is_backpack_displayed()