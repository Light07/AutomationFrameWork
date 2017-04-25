__author__ = 'kevin'

import os
import traceback

def take_screenshot(func):

    def save_screenshot(self):
        class_name = self.__class__.__name__
        print (class_name)
        try:
            func(self)
        except Exception as e:
            path = os.path.dirname(os.path.abspath(__file__))
            print (path)
            path = path.split("\common")[0]
            path += "\screenshots_logs"
            if not os.path.exists(path):
                os.mkdir(path)
            self.browser.save_screenshot("%s/%s_screenshot.jpg" % (path,class_name))
            #Save the Error Stack Information
            log_file = open("%s/%s.log" %(path,class_name),"a")
            log_file.write(traceback.format_exc())
            print (traceback.format_exc())

            raise e

    return save_screenshot