#coding=utf-8

import unittest

from common.selenium_helper import SeleniumHelper
from common.take_screenshot import take_screenshot
from page.baidu import BAI_DU

# @unittest.skip("skip")
class Test_Baidu(unittest.TestCase):
    def setUp(self):
        self.browser = SeleniumHelper.open_browser("firefox")

    # @unittest.skip("not run")
    @take_screenshot
    def test_baidu_search(self):
        """Test search"""
        baidu = BAI_DU(self.browser)
        baidu.search()
        assert 1==1

    @take_screenshot
    def test_baidu_set(self):
        """Test set preference"""
        baidu = BAI_DU(self.browser)
        baidu.preferences()
        assert 1==1

    def tearDown(self):
        self.browser.delete_all_cookies()
        self.browser.quit()

if __name__ == "__main__":

    def suite():
        return unittest.makeSuite(Test_Baidu, "test")
    unittest.main(defaultTest = 'suite')
