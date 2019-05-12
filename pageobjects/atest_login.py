# coding=utf-8
import time

from framework.base_page import BasePage


class HomePage(BasePage):
    input_box = "name=>name"
    input1_box = "name=>password"

    search_btn = "name=>submit"



    def type_input(self, in_text,in_text1):
        time.sleep(3)
        self.type(self.input_box, in_text)
        self.type(self.input1_box,in_text1)


    def send_submit_btn(self):
        self.click(self.search_btn)
        self.sleep(2)
