import time

import pytest

from pom.tests.test_base import TestBase
from pom.utilities import excel_reader


class TestProduct(TestBase):


    def test_no_of_items_available(self):
        self.loginPage.perform_login("standard_user","secret_sauce")
        assert self.productPage.count_no_of_items()  == 6


    def test_added_all_items(self):
        self.loginPage.perform_login("standard_user","secret_sauce")
        assert self.productPage.add_all_items_to_basket()==6

    def test_product_sort(self):
        self.loginPage.perform_login("standard_user", "secret_sauce")
        excel_reader.load_xl("C:\\Users\mages\\PycharmProjects\\SeleniumPythonFramework\\test_data.xlsx", "data")
        data=excel_reader.get_data_as_list_of_tuples()
        print(data)
        for item in data:
            self.productPage.select_item(item[0])
            time.sleep(2)
            assert self.productPage.get_first_item_name() == item[1]
            assert self.productPage.get_first_item_price()=='$'+str(item[2])
