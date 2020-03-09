import unittest
import HtmlTestRunner

def run_html(test_name, test_case, add_timestamp=False):
    suite = None
    if isinstance(test_case, list):
        suite = unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(x) for x in test_case])
    else:
        suite = unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(test_case)])
    
    runner = HtmlTestRunner.HTMLTestRunner(
        verbosity=2,
        report_title="Test Report: %s" % test_name,
        report_name=test_name,
        output="reports",
        add_timestamp=add_timestamp
    )
    runner.run(suite)