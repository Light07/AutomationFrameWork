__author__ = 'kevin'

from hamcrest import assert_that
from hamcrest import contains_string
from robot.utils.asserts import assert_equal
from selenium.webdriver.common.keys import Keys

from common.selenium_helper import SeleniumHelper
import settings

class LoginPage(object):
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(settings.B2S_URL)

    def error_username_message(self):
        error_username = self.browser.find_element_by_id("msg-username")
        return error_username.text

    def error_password_message(self):
        error_password = self.browser.find_element_by_id("msg-password")
        return error_password.text

    def invalid_user_login_validation(self):
        error_info = self.error_username_message()
        assert_equal(error_info, 'Wrong email or password')

    def blank_user_login_validation(self):
        error_info = self.error_username_message()
        assert_equal(error_info, 'Please enter your email')
        error_info = self.error_password_message()
        assert_equal(error_info, 'Please enter your password')

    def expired_user_login_validation(self):
        error_info = self.error_username_message()
        assert_equal(error_info, 'Account expired')

    def login(self, user_name, password):
        user_element = self.browser.find_element_by_id("username")
        user_element.send_keys(user_name)
        password_element = self.browser.find_element_by_id("password")
        password_element.send_keys(password +Keys.RETURN)

    def valid_login_validation(self):
        SeleniumHelper.wait_until_element_is_displayed(self.browser, "//div/div/ul/li/a/i[@class='ue-header-icons ue-home']")
        currentUrl = self.browser.current_url
        assert_that(currentUrl, contains_string('school/elab/mypage'))