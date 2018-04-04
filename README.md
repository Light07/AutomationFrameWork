# Generic automationFrameWork on behalf of [ptest](https://pypi.python.org/pypi/ptest)

### Basic Usage:
1. Decorate your test class with decorator @TestClass, @Test, @BeforeMethod.
* @TestClass - a test class eg: @TestClass(run_mode="parallel")
* @Test - a single test eg: @Test(tags=["regression", "smoke"])
* @BeforeMethod - a method executed before a test run. eg:@BeforeMethod(description="Prepare test data.")
* @AfterMethod - a method executed after a test run. eg:@AfterMethod(always_run=True, description="Clean up")

2. Run like below
* >Python 2.x:
 $ ptest -w c:\folder -t test.test_baidu -i "smoke" -n 2

 Python 3.x:
 $ ptest3 -w c:\folder -t test.test_baidu -i "smoke" -n 2

* -w -the workspace
* -t -the target to run
* -i -tags defined next to @Test
* -n The number of test executors, work along with run_mode, if "parallel", run parallelly, otherwise run cases one by one.

you can run by package/module/class/method/tags which are very flexible for your test,more usage, please refer to [ptest](https://pypi.python.org/pypi/ptest)

3. After run, a test report will generated with detail info, any failed cases will attached along with a sceeen shot.

* Overview report

![Overview Report](http://i4.bvimg.com/639741/b46b3a6032afef3b.jpg)

* Detail report

![Detail Report](http://i4.bvimg.com/639741/10d8ab91e1257714s.jpg)

