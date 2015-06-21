__author__ = 'kevin'
#coding=utf-8

import  time

import settings
from settings.test_config import DEFAULT_SLEEP_TIME

class BAI_DU(object):
    def __init__(self, browser):
        self.browser = browser

    def search(self):
        browser = self.browser
        browser.get(settings.BAI_DU_HOME + "/")
        browser.find_element_by_id("kw").send_keys("selenium webdriver")
        browser.find_element_by_id("su").click()
        time.sleep(DEFAULT_SLEEP_TIME)
        browser.close()

    def preferences(self):
        browser = self.browser
        browser.get(settings.BAI_DU_HOME + "/gaoji/preferences.html")
        member_count=browser.find_element_by_xpath(".//*[@id='nr']")
        member_count.find_element_by_xpath("//option[@value='10']").click()
        time.sleep(DEFAULT_SLEEP_TIME)
        browser.find_element_by_xpath(".//*[@id='save']").click()
        time.sleep(DEFAULT_SLEEP_TIME)
        browser.switch_to_alert().accept()