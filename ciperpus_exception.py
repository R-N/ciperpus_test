from enum import Enum, auto
import sys

class ciperpus_error_code(Enum):
	pass

class general_error_code(ciperpus_error_code):
	unknown = auto()

	def message(self):
		if self == general_error_code.unknown: return "Error tidak diketahui"
		raise ValueError("Invalid login exception code")
	@property
	def full_name(self):
		return "%s.%s" % (self.__class__.__name__, self.name)

class ciperpus_exception(Exception):
	#https://stackoverflow.com/questions/6180185/custom-python-exceptions-with-error-codes-and-error-messages
	def __init__(self, error_code, message='', *args, **kwargs):
		if not isinstance(error_code, ciperpus_error_code):
			raise ValueError("Invalid error code")
		self.error_code = error_code

		self.traceback = sys.exc_info()
		if message == '':
			message = error_code.message()
		try:
			msg = '[{0}] {1}'.format(error_code.name, message.format(*args, **kwargs))
		except (IndexError, KeyError):
			msg = '[{0}] {1}'.format(error_code.name, message)

		super().__init__(msg)


class login_error_code(ciperpus_error_code):
	username_kosong = auto()
	password_kosong = auto()
	username_password_kosong = auto()
	user_tidak_ada = auto()
	username_password_salah = auto()

	def message(self):
		if self == login_error_code.username_kosong: return "Username tidak boleh kosong"
		if self == login_error_code.password_kosong: return "Password tidak boleh kosong"
		if self == login_error_code.username_password_kosong: return "Username dan password tidak boleh kosong"
		if self == login_error_code.user_tidak_ada: return "User tidak terdaftar"
		if self == login_error_code.username_password_salah: return "Username atau password salah"
		raise ValueError("Invalid login exception code")
	@property
	def full_name(self):
		return "%s.%s" % (self.__class__.__name__, self.name)

class login_exception(ciperpus_exception):

	def __init__(self, error_code, *args, **kwargs):
		if not isinstance(error_code, login_error_code):
			raise ValueError("Invalid error code")

		super().__init__(error_code, error_code.message())