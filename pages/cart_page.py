from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    backpack = (By.ID, "item_4_title_link")
    checkout_button = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_backpack_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.backpack)
        ).is_displayed()

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()