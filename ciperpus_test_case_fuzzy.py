import unittest
from ciperpus_test_logic import *
from ciperpus_util import *
import fuzzing
import ciperpus_generation_fuzzer

class ciperpus_test_case_fuzzy(unittest.TestCase):

	def setUp(self):
		self.logic =  get_logic()

	def test_login(self):
		valid_login = {
			"admin": "admin"
		}
		cases = zip_lists((
			ciperpus_generation_fuzzer.fuzz_string(100, 100), 
			ciperpus_generation_fuzzer.fuzz_string(100, 100)
		))
		for case in cases:
			username, password = case
			with self.subTest(msg="Test login: %s" % list_to_string(case)):
				data =  {
					"username": username,
					"password": password,
					"use_button": True,
					"valid_login": valid_login
				}
				self.logic.login(self, data)
