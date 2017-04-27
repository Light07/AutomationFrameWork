#coding=utf-8

from ptest.assertion import assert_that, assert_equals
from ptest.decorator import TestClass, BeforeMethod, Test, AfterMethod
from ptest.plogger import preporter

from common.selenium_helper import SeleniumHelper
from page.baidu import BAI_DU


@TestClass(run_mode='parallel')
class TestBaidu:
    @BeforeMethod(description="prepare test data")
    def before(self):
        preporter.info("Test is about to start")
        self.browser = SeleniumHelper.open_browser("chrome")

    @Test(tags =["regression", "smoke"])
    def test_baidu_search(self):
        """Test search"""
        baidu = BAI_DU(self.browser)
        baidu.search("test")
        assert_equals(1, 1)

    @Test(tags =["regression", "smoke"])
    def test_baidu_set(self):
        """Test set preference"""
        baidu = BAI_DU(self.browser)
        baidu.preferences()
        assert_equals(1, 0)

    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        preporter.info("Cleaning up")
        self.browser.delete_all_cookies()
        self.browser.quit()