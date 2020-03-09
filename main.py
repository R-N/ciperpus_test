from ciperpus_test_logic import ciperpus_test_logic
from ciperpus_exception import *
from ciperpus_test_exception import *
from ciperpus_test_context import *
from ciperpus_test_case import ciperpus_test_case
from ciperpus_test_case_fuzzy import ciperpus_test_case_fuzzy
from ciperpus_db_client import *
import ciperpus_test_runner


if __name__ == '__main__':
    with get_db_client() as db_client:
        db_client.reset()
    ciperpus_test_runner.run_html("Normal Tests", ciperpus_test_case)
    ciperpus_test_runner.run_html("Fuzzy Tests", ciperpus_test_case_fuzzy)