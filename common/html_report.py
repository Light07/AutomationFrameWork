__author__ = 'kevin'

import os
import HTMLTestRunner

class Generate_Report():
        def __init__(self):
            self.test_base =os.path.dirname(os.path.dirname(__file__))
            if os.path.exists(os.path.join(self.test_base,"test_report.html")):
                os.remove(os.path.join(self.test_base,"test_report.html"))
            fp = open(os.path.join(self.test_base,"test_report.html"),"a")
            fp.close()
        def generate_report(self, test_suites):
            fp = file(os.path.join(self.test_base,"test_report.html"),"a")
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="TestReport",\
                                                   description="Below report show the results of auto run")
            runner.run(test_suites)