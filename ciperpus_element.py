from selenium import webdriver

class ciperpus_element:
    def __init__(self, element, driver):
        self.element = element
        self.driver = driver

    @property
    def client(self):
        return self.driver.client

    def click(self):
        return self.element.click()

    def clear(self):
        return self.element.clear()

    def find_element(self, selector):
        return ciperpus_element(self.page.find_element_by_css_selector(selector), self.driver)

    def find_elements(self, selector):
        return [ciperpus_element(el, self.driver) for el in self.page.find_element_by_css_selector(selector)]

    def attr(self, attr):
        return self.element.get_attribute(attr)

    def prop(self, prop):
        return self.element.get_property(prop)

    def css(self, attr):
        return self.element.value_of_css_property(attr)

    @property
    def is_displayed(self):
        return self.element.is_displayed()

    @property
    def is_enabled(self):
        return self.element.is_enabled()

    @property
    def is_selected(self):
        return self.element.is_selected()

    @property
    def text(self):
        return self.element.text

    @property
    def size(self):
        return self.element.size

    @property
    def tag_name(self):
        return self.element.tag_name

    def screenshot(self, filename):
        return self.element.screenshot(filename)

    def send_keys(self, value):
        return self.element.send_keys(value)

    def submit(self):
        return self.element.submit()
