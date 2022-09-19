import pytest
import unittest
from pages.Home.signup_pages import SignupPage
from pages.Home.fangate_pages import FangatePage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SignupTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sp = SignupPage(self.driver)
        self.fp = FangatePage(self.driver)


    def test_validSignup(self):
        self.fp.devUnlock("testdev123")
        self.sp.signup("anil", "sharma", "anilverma1000000000@baltech.in", "123456")
