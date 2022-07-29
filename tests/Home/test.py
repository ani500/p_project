import time

import pytest
import unittest

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
        wait = WebDriverWait(self.sd.driver,10)
        original_window = self.sd.driver.current_window_handle
        assert len(self.sd.driver.window_handles) == 1
        time.sleep(5)
        self.sd.driver.refresh()
        self.sd.driver.find_element(By.LINK_TEXT, "Register now!").click()
        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in self.sd.driver.window_handles:
            if window_handle != original_window:
                self.sd.driver.switch_to.window(window_handle)
                break

        wait.until(EC.title_is("Selenium Conf 2022 - Online | ConfEngine - Conference Platform"))











