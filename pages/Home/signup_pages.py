import time
from base.selenium_driver import SeleniumDriver

class SignupPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    #Locators
    _signup_link = "Sign Up"
    _first_name = "signup_first_name"
    _last_name = "signup_last_name"
    _signup_email = 'signup_email'
    _signup_pwd = "signup_password"
    _confirm_checkbox ="//div[@class='checkbox']//label[@for='confirm_checkbox']"
    _confirm_checkbox_id = "confirm_checkbox"
    _signup_button= "//button[text()='CREATE TRIAL ACCOUNT']"

    def clickOnTheSignupLink(self):
        self.elementClick(self._signup_link, "link")

    def waitFl(self,loc,lid="id"):
        self.waitForElement(loc,lid,20,.5)

    def firstNameSendKeys(self, fName):
        self.sendKeys(fName, self._first_name)

    def lastNameSendKeys(self, lName):
        self.sendKeys(lName, self._last_name)

    def emailSendKeys(self, email):
        self.sendKeys(email, self._signup_email)

    def passwordSendKeys(self, pwd):
        self.sendKeys(pwd, self._signup_pwd)

    def clickConfirm(self):
        self.checkRadioElementClick(self._confirm_checkbox, "xpath", self._confirm_checkbox_id)

    def clickOnSignupButton(self):
        self.elementClick(self._signup_button,'xpath')

    def signup(self, firstname, lastname, email, password):
        time.sleep(10)
        self.waitFl(self._signup_link,'link')
        self.clickOnTheSignupLink()
        self.waitFl(self._first_name)
        self.firstNameSendKeys(firstname)
        self.lastNameSendKeys(lastname)
        self.emailSendKeys(email)
        self.passwordSendKeys(password)
        time.sleep(5)
        self.clickConfirm()
        self.waitFl(self._signup_button,'xpath')
        self.clickOnSignupButton()
















