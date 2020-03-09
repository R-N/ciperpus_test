from ciperpus_exception import *
from ciperpus_test_exception import *
from ciperpus_test_context import *
from ciperpus_client import ciperpus_client
import unittest

class ciperpus_test_logic:
    def __init__(self, client=None):
        if client is None:
            self.client = ciperpus_client()
        else:
            self.client = client

    def login(self, case, data):
        username = data["username"]
        password = data["password"]
        valid_login = data["valid_login"]
        expect_error = None
        if username == "":
            if password == "":
                expect_error = login_error_code.username_password_kosong
            else:
                expect_error = login_error_code.username_kosong
        elif password == "":
            expect_error = login_error_code.password_kosong
        elif username not in valid_login:
            expect_error = login_error_code.user_tidak_ada
        elif valid_login[username] != password:
            expect_error = login_error_code.username_password_salah
        with ciperpus_test_context_case(case, expect_error) as context:
            self.client.login(username, password, data["use_button"])

    
    def logout(self, expect_error=None):
        with ciperpus_test_context(expect_error) as context:
            self.client.logout()

    def dashboard(self, expect_error=None):
        with ciperpus_test_context(expect_error) as context:
            self.client.logout()

    @property
    def url(self):
        return self.client.url


    def check_url(self, endpoint):
        return self.client.check_url(endpoint)

    def close(self):
        return self.client.close()

    def quit(self):
        return self.client.quit()

    def __enter__(self): 
        return self
  
    def __exit__(self, exc_type, exc_value, traceback): 
        self.quit() 

logic_instance = None

def get_logic():
    global logic_instance
    logic_instance = logic_instance or ciperpus_test_logic()
    return logic_instance
    