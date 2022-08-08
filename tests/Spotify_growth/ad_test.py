import pytest
import unittest
from pages.Home.login_pages import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AdTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)

    @pytest.mark.order2
    def test_AdCreate(self):
        print("running createfnagate")
        self.fp.devUnlock("testdev123")
        self.lp.login("anil@baltech.in", "123456")
