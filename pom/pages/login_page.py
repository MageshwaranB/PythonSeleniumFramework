from selenium.webdriver.common.by import By
from pom.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage(BasePage):
    username_txt_box = (By.ID, "user-name")
    password_txt_box = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    accepted_usernames = (By.XPATH, "//div[@id='login_credentials']")
    error_message = (By.XPATH, "//div[@class='error-message-container error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @staticmethod
    def __separate_usernames(names: str):
        name = names.split(":")
        return name

    def get_available_usernames(self):
        return self.__separate_usernames(self.get_text(self.accepted_usernames))

    def perform_login(self, username, password):
        self.enter_text(self.username_txt_box, username)
        self.enter_text(self.password_txt_box, password)
        self.click(self.login_btn)

    def epic_sad_face(self) -> str:
        return self.get_text(self.error_message)
