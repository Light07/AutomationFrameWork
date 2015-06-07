# __author__ = 'kevin'
# #coding = utf8
#
# import  unittest,time,re
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui  import Select
# from selenium.common.exceptions import NoSuchElementException
#
# from common.take_screenshot import take_screenshot

# class Github(unittest.TestCase):
#     def setUp(self):
#         self.verificationErrors = []
#         self.accept_next_alert = True
#         default = "C:\Users\kevin\AppData\Roaming\Mozilla\Firefox\Profiles\dx2bpjh3.default"
#         profile = webdriver.FirefoxProfile(default)
#         self.browser = webdriver.Firefox(profile)
#         self.browser.implicitly_wait(30)
#         self.base_url = "https://github.com"
#         self.browser.get(self.base_url + "/login")
#         self.browser.find_element_by_id("login_field").send_keys("light07")
#         self.browser.find_element_by_id("password").send_keys("P@ssw0rd")
#         self.browser.find_element_by_id("password").send_keys(Keys.ENTER)
#         time.sleep(2)
#
#     @take_screenshot
#     def test_access_sucess(self):
#         browser = self.browser
#         assert browser.find_element_by_xpath(".//*[@id='user-links']/li[1]/a/span/span").is_displayed() is True
#
#     @take_screenshot
#     def test_search(self):
#         browser = self.browser
#         browser.find_element_by_xpath("html/body/div[1]/div[1]/div/div/form/label/input").send_keys("requests")
#         browser.find_element_by_xpath("html/body/div[1]/div[1]/div/div/form/label/input").send_keys(Keys.ENTER)
#         time.sleep(2)
#         status = browser.find_element_by_xpath(".//*[@id='container']/div[2]/div/div[2]/ul/li[1]/h3/a").is_displayed()
#         assert status is True
#         browser.find_element_by_xpath(".//*[@id='container']/div[2]/div/div[2]/ul/li[1]/h3/a").click()
#         time.sleep(2)
#         assert browser.current_url == "https://github.com/kennethreitz/requests"
#
#     def tearDown(self):
#         browser = self.browser
#         browser.delete_all_cookies()
#         browser.close()
#
# # if __name__ == "__main__":
# #     unittest.main()
# #

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from common.take_screenshot import take_screenshot


class Baidu(unittest.TestCase):
    def setUp(self):
        default = "C:\Users\kevin\AppData\Roaming\Mozilla\Firefox\Profiles\dx2bpjh3.default"
        profile = webdriver.FirefoxProfile(default)
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    @take_screenshot
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    @take_screenshot
    def test_baidu_set(self):
        driver = self.driver
        driver.get(self.base_url + "/gaoji/preferences.html")
        m=driver.find_element_by_xpath(".//*[@id='nr']")
        m.find_element_by_xpath("//option[@value='10']").click()
        time.sleep(2)

        driver.find_element_by_xpath(".//*[@id='save']").click()
        time.sleep(2)
        driver.switch_to_alert().accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    def suite():
        return unittest.makeSuite(Baidu, "test")

    unittest.main(defaultTest = 'suite')
