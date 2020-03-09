from ciperpus_driver import ciperpus_driver
from ciperpus_page import *
from ciperpus_exception import *
from functools import wraps
import enum

class ciperpus_client():
    def __init__(self, base_url="http://localhost/ciperpus", headless=False, default_username="admin", default_password = "admin"):
        self.base_url = base_url
        self.driver = ciperpus_driver(self, headless)
        self.page = ciperpus_page(self)
        self.is_logged_in = False
        self.default_username = default_username
        self.default_password = default_password

    def require_login(foo):
        @wraps(foo)
        def wrap(self, *args, **kwargs):
            if not self.is_logged_in:
                self.login()
            return foo(self, *args, **kwargs)
        return wrap

    def require_logout(foo):
        @wraps(foo)
        def wrap(self, *args, **kwargs):
            if self.is_logged_in:
                self.logout()
            return foo(self, *args, **kwargs)
        return wrap

    @require_logout
    def login(self, username=None, password=None, use_button=True):
        if username is None:
            username = self.default_username
        if password is None:
            password = self.default_password
        self.page.login()
        username_field = self.driver.find("#inputEmail3")
        if username_field is None:
            raise ciperpus_exception(general_error_code.unknown)
        username_field.click()
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.driver.find("#inputPassword3")
        password_field.clear()
        password_field.click()
        password_field.send_keys(password)
        if use_button:
            sign_in_button = self.driver.find("#btn-sign-in")
            sign_in_button.click()
        else:
            password_field.submit()
        result = self.check_url(endpoints.dashboard)
        if result:
            self.is_logged_in = True
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
    
    @require_login
    def logout(self):
        self.page.logout()
        self.is_logged_in = False
        return True

    @property
    def url(self):
        return self.driver.url

    def to_url(self, endpoint):
        ret = endpoint
        if not endpoint.startswith("http"):
            ret = "%s/%s" % (self.base_url, endpoint)
        return ret

    def check_url(self, endpoint):
        url = self.to_url(endpoint)
        cur_url = self.driver.url
        if cur_url == endpoint:
            return True
        if len(url) != len(cur_url):
            return False
        url = url[len(self.base_url):]
        cur_url = cur_url[len(self.base_url):]
        return url == cur_url

    def close(self):
        return self.driver.close()

    def quit(self):
        return self.driver.quit()

    def __enter__(self): 
        return self
  
    def __exit__(self, exc_type, exc_value, traceback): 
        self.quit() 

client_instance = None

def get_client():
    global client_instance
    client_instance = client_instance or ciperpus_client()
    return client_instance