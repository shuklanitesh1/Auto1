import time

import pytest
from selenium.webdriver.common.by import By

from Config.config import Testdata
from Pages.StartPage import StartPage
from Test.test_base import BaseTest


# @pytest.mark.usefixtures["init_driver"]  # fixture can be directly used like this as well
class Test_Search_Auto1(BaseTest):

    def test_search(self):
        self.search = StartPage(self.driver)
        self.search.auto_search()
        self.driver.implicitly_wait(3)

    def test_brand_model(self):
        self.brand_verify = StartPage(self.driver)
        self.brand_verify.brand_model_verification()



