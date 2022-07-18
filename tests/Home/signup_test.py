import pytest
import unittest
from pages.Home.login_pages import LoginPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SignupTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    def test_validSignup(self):
        self.lp.signup("anil", "sharma", "anil@baltech.in", "123456")
