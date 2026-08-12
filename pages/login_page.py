from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import get_logger


class LoginPage:

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(__name__)

    def enter_username(self, username):

        self.logger.info("Entering username")

        self.wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(username)

    def enter_password(self, password):

        self.logger.info("Entering password")

        self.wait.until(
            EC.visibility_of_element_located(self.password)
        ).send_keys(password)

    def click_login(self):

        self.logger.info("Clicking login button")

        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def get_error_message(self):

        self.logger.info("Getting login error message")

        return self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        ).text