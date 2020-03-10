from ciperpus_test_exception import *
from ciperpus_exception import *

class ciperpus_test_context:
	def __init__(self, expect_error=None):
		self.expect_error = expect_error

	def __enter__(self):
		pass
		
	def __exit__(self, exc_type, ex, exc_traceback):
		if ex:
			if not isinstance(ex, ciperpus_exception):
				return
			elif self.expect_error is None:
				raise ciperpus_test_exception(ciperpus_test_error_code.unexpected_exception, (ex.error_code.full_name,))
			elif ex.error_code != self.expect_error:
				raise ciperpus_test_exception(ciperpus_test_error_code.wrong_exception, (self.expect_error.full_name, ex.error_code.full_name,))
			else:
				return True
		else:
			if self.expect_error is not None:
				raise ciperpus_test_exception(ciperpus_test_error_code.expected_exception, (self.expect_error.full_name,))

class ciperpus_test_context_case(ciperpus_test_context):
	def __init__(self, case, expect_error=None):
		self.case = case
		super().__init__(expect_error)

	def __exit__(self, *args, **kwargs):
		try:
			return super().__exit__(*args, **kwargs)
		except ciperpus_test_exception as ex:
			self.case.fail(str(ex))
			return True

class ciperpus_test_print_only:
	def __init__(self, expect_error=None):
		self.expect_error = expect_error

	def __enter__(self):
		pass
		
	def __exit__(self, exc_type, ex, exc_traceback):
		if exc_type:
			print(ex)
			return True