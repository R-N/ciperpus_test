from enum import Enum, auto
import sys

class ciperpus_test_error_code(Enum):
	unexpected_exception = auto()
	wrong_exception = auto()
	expected_exception = auto()

	def message(self):
		if self == ciperpus_test_error_code.unexpected_exception: return "Tes seharusnya berjalan lancar. Didapat exception: %s"
		if self == ciperpus_test_error_code.wrong_exception: return "Tes mengharapkan exception %s. Didapat exception: %s"
		if self == ciperpus_test_error_code.expected_exception: return "Tes mengarapkan exception %s tapi berjalan lancar."
		raise ValueError("Invalid test exception code")
	
	@property
	def full_name(self):
		return "%s.%s" % (self.__class__.__name__, self.name)

class ciperpus_test_exception(Exception):
	#https://stackoverflow.com/questions/6180185/custom-python-exceptions-with-error-codes-and-error-messages
	def __init__(self, error_code, arg, *args, **kwargs):
		if not isinstance(error_code, ciperpus_test_error_code):
			raise ValueError("Invalid error code")
		self.error_code = error_code

		self.traceback = sys.exc_info()
		message = error_code.message() % arg
		super().__init__(message)