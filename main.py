
from ciperpus_exception import *
from ciperpus_test_exception import *
from ciperpus_test_case import ciperpus_test_case
from ciperpus_test_case_fuzzy import ciperpus_test_case_fuzzy
from ciperpus_test_case_payload import ciperpus_test_case_payload
import ciperpus_db_client
from ciperpus_util import *
import ciperpus_test_runner
import ciperpus_client


if __name__ == '__main__':
	mkdir("cases")
	mkdir("payloads")
	mkdir("reports")
	with ciperpus_db_client.get_db_client() as db_client:
		db_client.reset()
	with ciperpus_client.create_client() as client:
		ciperpus_test_runner.run_html("Normal Tests", ciperpus_test_case)
		ciperpus_test_runner.run_html("Fuzzy Tests", ciperpus_test_case_fuzzy)
		ciperpus_test_runner.run_html("Payload Tests", ciperpus_test_case_payload)
	