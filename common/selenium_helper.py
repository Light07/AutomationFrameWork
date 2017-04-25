__author__ = 'kevin'

import time

import urllib
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException

from settings.test_config import PROXY,FIRE_PROFILE, FIND_ELEMENT_TIMEOUT,DEFAULT_SLEEP_TIME,TIMEOUT

class SeleniumHelper(object):
    @staticmethod
    def getStatusCode(self, url):
        return urllib.urlopen(url).getcode(0)

    @staticmethod
    def assertCurrentUrl(self, string, environment):
        currentUrl = self.browser.current_url
        assert_that(currentUrl).contains(environment)
        assert_that(self.getStatusCode(currentUrl)).equal_to(200)
        assert_that(currentUrl).contains(string)

    @staticmethod
    def open_browser(browser_name, chrome_proxy=None, firefox_profile=None,ie_proxy=None):
        browser_name = browser_name.lower()

        if not browser_name in {'chrome', 'firefox', 'ff', 'ie', 'phantomjs'}:
            browser_name = 'chrome'

        if browser_name == 'ie':
              browser = webdriver.Ie()
        elif browser_name == 'chrome':
            if chrome_proxy:
                chrome_options_with_proxy = webdriver.ChromeOptions()
                proxy = PROXY
                chrome_options_with_proxy.add_argument('--proxy-server=http://%s' %proxy)
                browser = webdriver.Chrome(chrome_options=chrome_options_with_proxy)
            else:
                browser = webdriver.Chrome()

        elif browser_name == 'phantomjs':
            browser = webdriver.PhantomJS()

        elif browser_name in ('firefox', 'ff'):
            if firefox_profile:
                default=FIRE_PROFILE
                profile=webdriver.FirefoxProfile(default)
                browser=webdriver.Firefox(profile)
            else:
                browser = webdriver.Firefox()

        if browser_name in {'chrome', 'firefox', 'ff', 'ie'}:
            browser.maximize_window()
        else:
            browser.set_window_size(1024, 768)

        browser.implicitly_wait(60)
        return browser

    @staticmethod
    def switch_to_new_window(browser,old_handle_list=None):
        """
        this is used to switch to new window.
        Note: if there are only two windows, the old_handle_list can be the default value: None, the new window will be selected.
              if there are more than two windows, the old_handle_list should be the list of older window's handle, the new window will be selected
        """
        old_handle = browser.current_window_handle
        handles = browser.window_handles

        for handle in handles:
            if old_handle_list == None:
                if handle == old_handle:
                    print ("%s is the old window's handler") %(handle)
                else:
                    print ("%s is the new window's handler") %(handle)
                    break
            else:
                if handle in old_handle_list:
                    print ("%s is the old window's handler") %(handle)
                else:
                    print ("%s is the new window's handler") %(handle)
                    break

        browser.switch_to_window(handle)

    @staticmethod
    def hover(browser, element):
        ActionChains(browser).move_to_element(element).perform()

    @staticmethod
    def doubleClick(browser, element):
        ActionChains(browser).double_click(element).perform()

    @staticmethod
    def click(browser, element):
        ActionChains(browser).click(element).perform()

    @staticmethod
    def element_exists(browser, xpath_locator):
        try:
            browser.find_element_by_xpath(xpath_locator)
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_element_by_xpath(browser, xpath_locator):
        exist_flag = False
        elapsed_time = 0
        while (elapsed_time < FIND_ELEMENT_TIMEOUT) and (exist_flag is False):
            try:
                element = browser.find_element_by_xpath(xpath_locator)
                if element.is_displayed() is False:
                    time.sleep(DEFAULT_SLEEP_TIME)
                    elapsed_time += DEFAULT_SLEEP_TIME
                    continue
                exist_flag = True
            except NoSuchElementException:
                time.sleep(DEFAULT_SLEEP_TIME)
                elapsed_time += DEFAULT_SLEEP_TIME
            return element

    @staticmethod
    def text_exists(browser, text):
        try:
            browser.find_element_by_name(text)
            return True
        except Exception:
            return False

    @staticmethod
    def wait_until_element(browser, xpath_locator, timeout=TIMEOUT):
        time_waited = 0
        while (True):
            try:
                browser.find_element_by_xpath(xpath_locator)
                break
            except Exception:
                time.sleep(DEFAULT_SLEEP_TIME)
                time_waited += DEFAULT_SLEEP_TIME
                if time_waited <= timeout:
                    continue
                else:
                    break

    @staticmethod
    def wait_until_text_display(browser, xpath_locator, text, timeout=TIMEOUT):
        time_waited = 0
        while True:
            element_text = SeleniumHelper.get_element_text(browser, xpath_locator)
            if element_text == text:
                break
            else:
                time.sleep(DEFAULT_SLEEP_TIME)
                time_waited += DEFAULT_SLEEP_TIME
                if time_waited <= timeout:
                    continue
                else:
                    break

    @staticmethod
    def wait_until_element_exists(browser, element):
        WebDriverWait(browser, TIMEOUT).until(lambda x: x is not None, element)

    @staticmethod
    def wait_until_element_is_displayed(browser, xpath_locator):
        WebDriverWait(browser, TIMEOUT).until(lambda driver: driver.find_element_by_xpath(xpath_locator).is_displayed())

    @staticmethod
    def page_is_loaded(browser):
        time_waited = 0
        while browser.execute_script("return document.readyState") != "complete":
            if (time_waited > TIMEOUT):
                raise TimeoutException("Timeout when page loading for %s!" % TIMEOUT)
            time.sleep(DEFAULT_SLEEP_TIME)
            time_waited += DEFAULT_SLEEP_TIME

    @staticmethod
    def get_element_text(browser, xpath_locator):
        element = browser.find_element_by_xpath(xpath_locator)
        text = element.get_attribute("innerHTML")
        return text

    @staticmethod
    def element_exists_by_css_selector(browser, css_selector):
        try:
            browser.find_element_by_css_selector(css_selector)
            return True
        except Exception:
            return False

    @staticmethod
    def wait_until_element_disappers(browser, xpath_locator):
        time_waited = 0
        while (time_waited < TIMEOUT):
            loading_element = SeleniumHelper.element_exists(browser, xpath_locator)
            if (loading_element == False):
                break
            else:
                time.sleep(DEFAULT_SLEEP_TIME)
                time_waited += DEFAULT_SLEEP_TIME

    @staticmethod
    def wait_until_element_display_status(browser, xpath_locator, status):
        time_waited = 0
        while (time_waited < TIMEOUT):
            element = browser.find_element_by_xpath(xpath_locator)
            display_status = element.value_of_css_property('display')
            if (display_status == status):
                break
            else:
                time.sleep(DEFAULT_SLEEP_TIME)
                time_waited += DEFAULT_SLEEP_TIME

    @staticmethod
    def wait_page_login(self):
        time_waited = 0
        while (True):
            current_url = self.current_url
            try:
                assert_that(self.getStatusCode(current_url)).equal_to(200)
                break
            except Exception:
                time_waited += DEFAULT_SLEEP_TIME
                time.sleep(DEFAULT_SLEEP_TIME)
                if time_waited <= TIMEOUT:
                    continue
                else:
                    break