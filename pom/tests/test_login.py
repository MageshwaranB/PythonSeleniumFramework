from pom.tests.test_base import TestBase


class TestLogin(TestBase):
    def test_handle_login_with_valid_credentials(self):
        url=self.loginPage.perform_login("standard_user","secret_sauce")
        assert "inventory" in self.loginPage.get_url_text()

    def test_handle_login_with_invalid_credentials(self):
        url=self.loginPage.perform_login("locked_out_user","secret_sauce")
        assert "Epic sadface: Sorry, this user has been locked out." ==self.loginPage.epic_sad_face()