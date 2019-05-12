# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):
    input_box = "id=>kw"

    search_btn = "id=>su"



    def type_input(self, in_text):
        self.type(self.input_box, in_text)

    def send_submit_btn(self):
        self.click(self.search_btn)
        self.sleep(2)
