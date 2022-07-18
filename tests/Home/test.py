from base.webdriverfactory import WebDriverFactory


class testc():

    def fun1(self):
        driver = WebDriverFactory('firefox')
        lp = driver.getWebDriverInstance()


ff = testc()
ff.fun1()
