from ciperpus_exception import *
from ciperpus_test_exception import *
from ciperpus_test_context import *
from ciperpus_client import ciperpus_client

class ciperpus_test_client:
    def __init__(self, client=None):
        if client is None:
            self.client = ciperpus_client()
        else:
            self.client = client

    def login(self, username, password, expect_error=None, use_button=True):
        with ciperpus_test_context(expect_error) as context:
            self.client.login(username, password)
    
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
        
test_client_instance = None

def get_test_client():
    global test_client_instance
    test_client_instance = test_client_instance or ciperpus_test_client()
    return test_client_instance