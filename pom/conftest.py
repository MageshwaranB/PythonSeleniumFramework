import time

import pytest
from selenium import webdriver

from pom.pages.base_page import BasePage
from pom.pages.login_page import LoginPage
from pom.pages.page_product import ProductPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Enter the browser name in lowercase")


@pytest.fixture
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture
def get_driver(request, get_browser):
    _driver = None
    if get_browser == "chrome":
        _driver = webdriver.Chrome()
    elif get_browser == "edge":
        _driver = webdriver.Edge()
    _driver.get("https://www.saucedemo.com/")
    _driver.maximize_window()
    _driver.implicitly_wait(10)
    """initializing the login page, with the help of request fixture and making it at class level, using the 
    loginPage variable we 're able to access the LoginPage class properties and functions
    """
    request.cls.loginPage=LoginPage(_driver)
    request.cls.productPage=ProductPage(_driver)
    request.cls.driver = _driver  # common driver
    yield request.cls.driver
    time.sleep(2)
    request.cls.driver.quit()
