import os

import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2
        }
    )

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def login(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver is None:
            driver = item.funcargs.get("login")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}.png"
            )

            driver.save_screenshot(screenshot_path)

            print(f"\nScreenshot saved: {screenshot_path}")