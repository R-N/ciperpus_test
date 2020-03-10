import unittest
from ciperpus_test_logic import *
from ciperpus_util import *

class ciperpus_test_case_payload(unittest.TestCase):

	def setUp(self):
		self.logic =  get_logic()

	def test_login(self):
		valid_login = {
			"admin": "admin"
		}
		cases = zip_lists((
			read_payload("payloads/username.txt"), 
			read_payload("payloads/password.txt")
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
