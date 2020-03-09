from selenium import webdriver
from ciperpus_element import ciperpus_element
from selenium.common.exceptions import NoSuchElementException

class ciperpus_driver:
    def __init__(self, client, headless=False):
        self.client = client
        options = webdriver.firefox.options.Options()
        options.set_capability("headless", headless)
        self.driver = webdriver.Firefox(options=options)
        self.open()

    @property
    def base_url(self):
        return self.client.base_url

    def open(self, endpoint=""):
        self.driver.get(self.client.to_url(endpoint))

    def find_element(self, selector):
        try:
            return ciperpus_element(self.driver.find_element_by_css_selector(selector), self)
        except NoSuchElementException as ex:
            return None

    def find(self, selector):
        return self.find_element(selector)

    def find_elements(self, selector):
        try:
            return [ciperpus_element(el, self) for el in self.driver.find_elements_by_css_selector(selector)]
        except NoSuchElementException as ex:
            return []

    @property
    def url(self):
        return self.driver.current_url

    def close(self):
        return self.driver.close()

    def quit(self):
        return self.driver.quit()

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def delete_all_cookies(self):
        return self.driver.delete_all_cookies()

    def get_log(self, log_type):
        return self.driver.get_log(log_type)

    def screenshot(self, filename):
        #return self.driver.get_screenshot_as_file(filename)
        return self.driver.save_screenshot(filename)

    @property
    def switch_to(self):
        return self.switch_to

    @property
    def title(self):
        return self.driver.title

    @property
    def page_source(self):
        return self.driver.page_source

    def wait(self, seconds):
        return self.driver.implicitly_wait(seconds)

