from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator: tuple):
        self.wait.until(expected_conditions.presence_of_element_located(locator)).click()

    def enter_text(self, locator: tuple, value: str):
        self.wait.until(expected_conditions.presence_of_element_located(locator)).send_keys(value)

    def get_title(self) ->str:
        return self.driver.title

    def get_text(self, locator: tuple) -> str:
        return self.wait.until(expected_conditions.presence_of_element_located(locator)).text

    def get_url_text(self) -> str:
        return self.driver.current_url
