import time


class Page_Actions:

    def __init__(self, driver):
        self.driver = driver

    def find_el(self, el_id):
        return self.driver.find_element_by_id(el_id)

    def click_on_element(self, el_id):
        self.find_el(el_id).click()
        time.sleep(1)

    def fill_element(self, el_id, text):
        self.find_el(el_id).send_keys(text)

    def text_element(self, el_id):
        return self.find_el(el_id).text

    def find_els_by_cls(self, els_cls):
        return self.driver.find_elements_by_class_name(els_cls)

    def close_connection(self):
        self.driver.quit()
