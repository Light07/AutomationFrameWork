__author__ = 'kevin'

from hamcrest import assert_that
from hamcrest import contains_string
from robot.utils.asserts import assert_equal
from selenium.webdriver.common.keys import Keys
from page_objects import page_element

from common.selenium_helper import SeleniumHelper
from page.abstract_base_page import AbstractBasePage
import settings


class LoginPage(AbstractBasePage):

    ERROR_USERNAME_ID = "msg-username"
    ERROR_PASSWORD_ID = "msg-password"
    USER_ELEMENT_ID = "username"
    PASSWORD_ELEMENT = "password"
    LOGIN_XPATH =  "//div/div/ul/li/a/i[@class='ue-header-icons ue-home']"
    MY_PAGE_STRING = 'school/elab/mypage'
    error_username = page_element(id_=ERROR_USERNAME_ID)
    error_password = page_element(id_=ERROR_PASSWORD_ID)
    user_element = page_element(id_=USER_ELEMENT_ID)
    password_element = page_element(id_=PASSWORD_ELEMENT)

    def __init__(self, browser):
        self.browser = browser
        AbstractBasePage.__init__(self, browser)

    def is_target_page(self):
        return assert_that(self.browser.get(settings.B2S_URL), contains_string("/partner/elab"))

    def error_username_message(self):
        return self.error_username.text

    def error_password_message(self):
        return self.error_password.text

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
        self.user_element.send_keys(user_name)
        self.password_element.send_keys(password +Keys.RETURN)

    def valid_login_validation(self):
        SeleniumHelper.wait_until_element_is_displayed(self.browser, self.LOGIN_XPATH)
        currentUrl = self.browser.current_url
        assert_that(currentUrl, contains_string(self.MY_PAGE_STRING))