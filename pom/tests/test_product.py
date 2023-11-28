from pom.tests.test_base import TestBase


class TestProduct(TestBase):
    def test_no_of_items_available(self):
        self.loginPage.perform_login("standard_user","secret_sauce")
        assert self.productPage.count_no_of_items()  == 6

    def test_added_all_items(self):
        self.loginPage.perform_login("standard_user","secret_sauce")
        assert self.productPage.add_all_items_to_basket()==6

