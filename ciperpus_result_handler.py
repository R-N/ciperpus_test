from ciperpus_page import endpoints

class ciperpus_result_handler:
	def __init__(self, client):
		self.client = client
		
	@property
	def driver(self):
		return self.client.driver 
		
	def login(self):
		result = self.check_url(endpoints.dashboard)
		if result:
			self.client.is_logged_in = True
		else:
			alert = self.driver.find(".alert")
			if alert is not None:
				text = alert.text.lower()
				if "username" in text and "password" in text:
					raise login_exception(login_error_code.username_password_salah)
				if "user" in text:
					raise login_exception(login_error_code.user_tidak_ada)
			else:
				alerts = self.driver.find_elements(".peringatan")
				username_empty = len([x for x in alerts if "username" in x.text.lower()]) > 0
				password_empty = len([x for x in alerts if "password" in x.text.lower()]) > 0
				if username_empty:
					if password_empty:
						raise login_exception(login_error_code.username_password_kosong)
					else:
						raise login_exception(login_error_code.username_kosong)
				elif password_empty:
					raise login_exception(login_error_code.password_kosong)
				raise ciperpus_exception(general_error_code.unknown)