#06/15/2015
#Author: kevin cai (kevin.cai@outlook.com)
# Generic automationFrameWork
# How to use:
#1."Common":  --Common methods to facilitates the whole project.
#    --html_report: To generate HTML report after test cases run.
#    --SeleniumHelper:Encapsulate all the customized method related to selenium/webdriver.
#    --take_screenshot: Take screenshot when cases run failure.
#    --txt_report: Independent way to run all the cases under test and generate simple txt format report.
#2."Page": -- The page under test,in this file, only store the page related function/method/date instead of test cases.\
#            different page should have separated pages.
#     --baidu  test example
#     --b2s      .........
#3."Settings": --Global settings & configuration & global data.
#    --__init__: Specify the test environment & configuration
#    --data_source
#    --test config:
#4."test" -- Test cases inherited from pages, this is the cases under test.
#    -- All the test cases related to separate pages are listed here.
#
#
#5. "main"  -- Load & run all of the test cases defined in test folder.
    --System will automated search all the test method defined in test folder and run them.

#Note:
# If you want to skip some test or even the whole test class, just put @unittest.skip("description") \
#in front of test case/test class