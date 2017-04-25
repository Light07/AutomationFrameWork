import time

from abc import ABCMeta, abstractmethod
from DateTime import DateTime
from assertpy import assert_that
from page_objects import PageObject, PageElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings

class AbstractBasePage(PageObject):

    __metaclass__ = ABCMeta

    WAIT_FOR_SCROLL_TIME = 2

    def __init__(self, driver):
        # Don't change the variable name w. it's used by PageObject
        self.w = driver
        self.driver = driver
        assert_that(self.has_loaded()).is_equal_to(True)

    def has_loaded(self):
        try:
            return self.is_target_page()
        except NoSuchElementException:
            return False

    # This function will be implement by sub class
    @abstractmethod
    def is_target_page(self):
        pass

    def is_element_displayed_on_page(self, ele, timeout=settings.TIME_OUT):
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: ele.is_displayed())
            result = True
        except Exception:
            result = False
        return result

    def is_element_found(self, timeout, *by):
        try:
            if WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by)):
                status = True
        except Exception:
            status = False

        return status

    def is_element_enabled(self, timeout, *by):
        try:
            if WebDriverWait(self.driver, timeout).until(lambda driver: EC._find_element(driver, by)).is_enabled():
                status = True
        except Exception:
            status = False

        return status

    def is_element_present(self, timeout, *by):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by))
            result = True
        except Exception:
            result = False
        return result

    def wait_until_element_clickable(self, timeout, *by):
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(*by))

    def is_element_clickable(self, timeout, *by):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(*by))
            result = True
        except Exception:
            result = False
        return result

    def is_page_element_clickable(self, element, timeout=settings.TIME_OUT):
        try:
            result = WebDriverWait(self.driver, timeout).until(lambda driver: element.is_enabled() & element.is_displayed())
        except Exception:
            result = False
        return result

    def wait_until_element_disappear(self, xpath_locator, timeout=settings.TIME_OUT):
        time_waited = 0
        while (time_waited < timeout):
            loading_element = self.element_displayed(xpath_locator)
            if (loading_element == False):
                break
            else:
                time.sleep(settings.SEARCH_POLL_TIME)
                time_waited += settings.SEARCH_POLL_TIME

    def element_displayed(self, xpath_locator):
        try:
            status = self.driver.find_element_by_xpath(xpath_locator).is_displayed()
        except Exception :
            status = False

        return status

    def is_page_loaded(self, target_url_string, timeout=settings.TIME_OUT):
        time_waited = 0
        status = False

        while time_waited < timeout:
            url = self.driver.current_url
            if target_url_string in url:
                status = True
                break
            else:
                time.sleep(settings.SEARCH_POLL_TIME)
                time_waited += settings.SEARCH_POLL_TIME

        return status

    def move_to_element(self, ele):
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.move_by_offset(1, 1)
        action.perform()

    def element_exists(self, xpath):
        size = -1
        size = len(self.driver.find_elements_by_xpath(xpath))
        if size > 0:
            return True
        else:
            return False

    def refresh_page(self):
        self.driver.get(self.driver.current_url)
