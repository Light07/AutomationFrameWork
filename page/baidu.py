__author__ = 'kevin'
#coding=utf-8

import  time

from page_objects import page_element

import settings
from settings.test_config import DEFAULT_SLEEP_TIME
from page.abstract_base_page import AbstractBasePage

class BAI_DU(AbstractBasePage):
    SEARCH_DIALOG_ID = "kw"
    SEARCH_ICON_ID = "su"
    MEMBER_COUNT_XPATH = "//option[@value='10']"
    SAVE_XPATH = ".//*[@id='save']"

    search_input_dialog = page_element(id_=SEARCH_DIALOG_ID)
    search_icon = page_element(id_=SEARCH_ICON_ID)
    member_count = page_element(xpath=MEMBER_COUNT_XPATH)
    save_button = page_element(xpath=SAVE_XPATH)

    def __init__(self, browser):
        self.browser = browser
        AbstractBasePage.__init__(self, browser)

    def is_target_page(self):
        self.browser.get(settings.BAI_DU_HOME + "/")
        return self.is_element_displayed_on_page(self.search_icon)

    def search(self, search_string):
        self.search_input_dialog.send_keys(search_string)
        self.search_icon.click()
        time.sleep(DEFAULT_SLEEP_TIME)
        self.browser.close()

    def preferences(self):
        browser = self.browser
        browser.get(settings.BAI_DU_HOME + "/gaoji/preferences.html")
        self.member_count.click()
        time.sleep(DEFAULT_SLEEP_TIME)
        self.save_button.click()
        time.sleep(DEFAULT_SLEEP_TIME)
        browser.switch_to_alert().accept()