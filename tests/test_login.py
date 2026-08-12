import pytest

from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        (
            "wrong_user",
            "wrong_password",
            "Username and password do not match"
        ),
        (
            "locked_out_user",
            "secret_sauce",
            "locked out"
        ),
    ]
)
def test_invalid_login(driver, username, password, expected_message):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert expected_message in error_message


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "inventory" in driver.current_url