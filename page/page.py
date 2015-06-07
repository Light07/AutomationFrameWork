#coding=utf-8

import unittest, time

from selenium import webdriver

from common.take_screenshot import take_screenshot

class Baidu(unittest.TestCase):
    def setUp(self):
        default = "C:\Users\kevin\AppData\Roaming\Mozilla\Firefox\Profiles\dx2bpjh3.default"
        profile = webdriver.FirefoxProfile(default)
        self.browser = webdriver.Firefox(profile)
        self.browser.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    @take_screenshot
    def test_baidu_search(self):
        driver = self.browser
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    @take_screenshot
    def test_baidu_set(self):
        driver = self.browser
        driver.get(self.base_url + "/gaoji/preferences.html")
        m=driver.find_element_by_xpath(".//*[@id='nr']")
        m.find_element_by_xpath("//option[@value='10']").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='save']").click()
        time.sleep(2)
        driver.switch_to_alert().accept()

    def tearDown(self):
        self.browser.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    def suite():
        return unittest.makeSuite(Baidu, "test")
    unittest.main(defaultTest = 'suite')
