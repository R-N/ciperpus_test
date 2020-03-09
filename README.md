# ciperpus_test

Fuzzy and csv test case testing with Selenium, unittest, and HttpTestRunner.

**Ciperpus Interface**

Selenium firefox webdriver is abstracted into ciperpus_driver and ciperpus_element. ciperpus_client uses ciperpus_driver and acts kind of like an API for ciperpus. It defines interface to ciperpus' functionality. ciperpus_client and ciperpus_page uses each other; mainly, it's ciperpus_client using ciperpus_page to open pages called endpoints. Those endpoints may be accessed through ciperpus_page functions. Those pages may require login, described by @require_login decorator. Some pages require user being logged out. ciperpus_client may throw ciperpus_exception for errors such as username being empty when requesting login. ciperpus_exception is made of ciperpus_error_code and message defined by ciperpus_error_code. It is recommended to test using ciperpus_error_code.

**Database**

ciperpus_db_client acts as abstraction of and interface for ciperpus' database. Its main functionality is to reset database prior to testing. It may include direct functionality interface to database in the future.

**Testing**

Testing can be done directly using ciperpus_client, with help of ciperpus_test_context or ciperpus_test_client, or automated with ciperpus_test_logic.  ciperpus_test_context handles your expected exception (or no exception) by ciperpus_error_code and throws ciperpus_test_exception if it's not as expected. ciperpus_test_exception will contain ciperpus_test_error_code (unexpected, expected, or wrong exception) and the expected and/or actual ciperpus_error_code. ciperpus_test_client simply wraps ciperpus_client functions with ciperpus_test_context. ciperpus_test_logic takes a test case and data to be executed. ciperpus_test_logic examines the data given, determines the expected output then proceeds to test. ciperpus_test_logic uses ciperpus_test_context_case which is just a derivation of ciperpus_test_context that can handle the result into test case, failing it if it should fail.

Curently, there are two types of test cases, both using unittest. ciperpus_test_case loads tests from a csv located in a folder named "cases" and executes every test cases there. The tests are done as subtests. ciperpus_test_classes can use any testing methods mentioned in the previous paragraph. ciperpus_test_case_fuzzy also runs tests, but the tests are obtained through fuzzing. For now, only string fuzzing is supported using fuzzing library. Number and file fuzzing will be implemented in the future. ciperpus_test_case_fuzzy can only use ciperpus_test_logic for the obvious reason that you can't provide expected result for random inputs.

**Reporting**

Tests are executed by ciperpus_test_runner. ciperpus_test_runner uses HtmlTestRunner and will make html reports automatically in the reports folder.

**Prerequisites**

The required python packages is listed in requirements.txt. You can easily install it using pip with:
```
pip install requirements.txt
```

Other requirements are:
*  [ciperpus](https://gitlab.com/psi-rabu-kel-3/ciperpus) running locally at http://localhost/ciperpus. During development of this, ciperpus was hosted using [xampp](https://www.apachefriends.org/index.html) running php 5.6.
*  Selenium gecko driver in PATH environment. Official guide is [here](https://selenium-python.readthedocs.io/installation.html). Make sure to at least try the first example and have it working.

A little fix is needed for HttpTestRunner due to the random unicode characters generated through fuzzing. On result.py, at line 403 (by the time this is written), add encoding="utf-8" argument ([ref](https://github.com/oldani/HtmlTestRunner/issues/48)). So, from:

```
        with open(path_file, 'w') as report_file:
```
to:

```
        with open(path_file, 'w', encoding="utf-8") as report_file:
```

**Concerns**

This is also a program, which can have bugs. This automated testing program should also be tested. Yes, it may sound ironic or/and dumb. The test results may not be accurate due to bugs from this program.

**Todo**

*  Implement more functionality in ciperpus_client and ciperpus_page
*  Implement logical navigation for more realistic testing
*  Cover more test cases
*  Implement number and file fuzzing to support more test cases
*  Implement database interface, maybe, for real database checking for test case data validity

**Known Bugs**

*  Username validity check is inconsistent with the real environment due to MySQL unicode collation. At first, it may just seem simple upper/lower case program which can be fixed easily, but it actually involves characters like "Ã" considered as equal to "a".
*  You tell me.