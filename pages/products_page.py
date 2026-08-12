from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    products_title = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_products_page_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.products_title)
        ).is_displayed()

    def add_backpack_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.backpack)
        ).click()

    def click_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()