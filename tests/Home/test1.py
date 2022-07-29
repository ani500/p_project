import time

import pytest
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SeleniumTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup1(self):
        self.sd = SeleniumDriver(self.driver)

    def test_Windows(self):
        time.sleep(2)
        iframe = self.sd.driver.find_element(By.TAG_NAME, "iframe")
        action = ActionChains(self.sd.driver)
        action.scroll_to_element(iframe)
        self.sd.driver.perform()
        action.
        time.sleep(5)














