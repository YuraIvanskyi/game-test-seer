import logging
import pytest
import allure

from models.Driver import AppiumDriver


@allure.step("Init Appium  driver")
@pytest.fixture(scope="session", autouse=True)
def driver(request):
    driver = AppiumDriver(capabilities, driver_conn_link).driver
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)

    @allure.step("End Appium  driver")
    def fin():
        logging.info("Closing driver instance")
        driver.close_app()
        driver.quit()

    yield driver
    request.addfinalizer(fin)


@pytest.fixture(scope="session", autouse=True)
def driver_conn_link():
    return "http://192.168.88.26:4723/wd/hub"


@pytest.fixture(scope="session", autouse=True)
def capabilities():
    return {
        "platformName": "iOS",
        "platformVersion": "15.6.1",
        "deviceName": "iPhone Yurii",
        "xcodeOrgId": "WFW2F3HSPA",
        "xcodeSigningId": "iPhone Developer",
        "automationName": "XCUITest",
        "udid": "00008030-001958AE01F3802E",
        "useNewWDA": False,
        "usePrebuiltWDA": True,
        "updatedWDABundleId": "i1skyi.WebDriverAgentRunner",
        "noReset": True,
        "falseRest": False,
        "showxcodeLog": True,
        "bundleId": "com.gameloft.dark.heroes.strategy.games",  # AgeOfVampires
    }
