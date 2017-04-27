__author__ = 'kevin'

from settings import blank_password, blank_user, invalid_user, invalid_password
from common.selenium_helper import SeleniumHelper
from page.b2s import LoginPage

from ptest.decorator import TestClass, Test, BeforeMethod, AfterMethod
from ptest.plogger import preporter

@TestClass(run_mode="parallel")  # the test cases in this class will be executed by multiple threads
class TestB2S:
    @BeforeMethod(description="Prepare test data.")
    def before(self):
        preporter.info("Test is about to start.")
        self.browser = SeleniumHelper.open_browser("chrome")

    @Test(tags="smoke, nightly")
    def test_blank_user_login(self):
        login = LoginPage(self.browser)
        login.login(blank_user, blank_password)
        login.blank_user_login_validation()

    @Test(tags="smoke, nightly")
    def test_invalid_user_login(self):
        login = LoginPage(self.browser)
        login.login(invalid_user, invalid_password)
        login.invalid_user_login_validation()

    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        preporter.info("cleaning up")
        self.browser.delete_all_cookies()
        self.browser.quit()