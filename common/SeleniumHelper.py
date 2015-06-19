__author__ = 'kevin.cai'

import urllib
from hamcrest import assert_that
from hamcrest import contains_string
from hamcrest import equal_to


class SeleniumHelper(object):

    def getStatusCode(self, url):
        return urllib.urlopen(url).getcode(0)

    def assertCurrentUrl(self, string, environment):
        currentUrl = self.browser.current_url
        assert_that(currentUrl, contains_string(environment))
        assert_that(currentUrl, contains_string(string))