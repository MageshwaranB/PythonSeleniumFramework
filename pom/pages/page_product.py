import pytest
from selenium.webdriver.common.by import By

from pom.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    all_items = (By.XPATH, "//div[@class='inventory_item']")
    product_text = (By.XPATH, "//div[@class='inventory_item_name']")
    cart_count=(By.XPATH,"//span[contains(@class,'shopping_cart_badge')]")

    def count_no_of_items(self):
        return self.get_elements_count(self.all_items)

    def add_all_items_to_basket(self):
        pytest.set_trace()
        for i in range(1,self.count_no_of_items()+1):
            self.click((By.XPATH,"//button[contains(@class,'btn_inventory')]["+str(i)+"]"))
        return int(self.get_cart_count())

    def get_cart_count(self):
        return self.get_text(self.cart_count)

