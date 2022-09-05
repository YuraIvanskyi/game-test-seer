from appium import webdriver


class AppiumDriver:
    class __AppiumDriver:
        def __init__(self, capabilities, driver_conn_link):
            self.driver = webdriver.Remote(
                command_executor=driver_conn_link,
                desired_capabilities=capabilities,
            )

    driver = None

    def __init__(self, capabilities, driver_conn_link):
        if not self.driver:
            AppiumDriver.driver = AppiumDriver.__AppiumDriver(
                capabilities, driver_conn_link
            ).driver
