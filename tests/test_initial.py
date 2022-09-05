import os
import allure
import pytest


@allure.title("Dummy valid")
def test_dummy_valid(driver):
    driver.save_screenshot(f'{os.path(os.getcwd(), "scr.png")}')


@pytest.mark.skip
@allure.title("Dummy invalid")
def test_dummy_invalid():
    assert 2
