from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    confirmation_message = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_customer_information(self, first_name, last_name, postal_code):

        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)

        self.wait.until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(last_name)

        self.wait.until(
            EC.visibility_of_element_located(self.postal_code)
        ).send_keys(postal_code)

    def click_continue(self):

        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def click_finish(self):

        self.wait.until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()

    def get_confirmation_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.confirmation_message)
        ).text