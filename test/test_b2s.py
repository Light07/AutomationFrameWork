__author__ = 'kevin'

import unittest

import  settings
from common.take_screenshot import take_screenshot
from common.selenium_helper import SeleniumHelper
from page.b2s import LoginPage

@unittest.skip("Won't Run")
class TestB2SLogin(unittest.TestCase):

    def setUp(self):
        self.browser =SeleniumHelper.open_browser("firefox")

    @take_screenshot
    def test_blank_user_login(self):
        login = LoginPage(self.browser)
        login.login(settings.blank_user,settings.blank_password)
        login.blank_user_login_validation()

    @take_screenshot
    def test_invalid_user_login(self):
        login = LoginPage(self.browser)
        login.login(settings.invalid_user,settings.invalid_password)
        login.invalid_user_login_validation()

    def tearDown(self):
        self.browser.delete_all_cookies()
        self.browser.quit()

if __name__ == "__main__":

    def suite():
        return unittest.makeSuite(TestB2SLogin, "test")
    unittest.main(defaultTest = 'suite')
