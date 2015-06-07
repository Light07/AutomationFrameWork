__author__ = 'kevin'

# from page.page import Github
# import unittest
#
# def suite():
#     return unittest.makeSuite(Github,"test")

# if __name__ == "__main__":
#     suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),"page"),pattern='*.py',top_level_dir=os.path.dirname(__file__))
#     unittest.TextTestRunner(verbosity=2).run(suite)


from page.page import Baidu
import unittest,os,re
from test.test import Test
from common.html_report import Generate_Report

# def suite():
#     return unittest.makeSuite(Baidu, "test")

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),"page"),pattern='*.py',top_level_dir=os.path.dirname(__file__))
    # unittest.TextTestRunner(verbosity=2).run(suite)
    html_report = Generate_Report()
    html_report.generate_report(suite)
    #
    # # test = Test()
    # # test.run_test()
