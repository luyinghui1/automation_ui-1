# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):
    input_box = "name=>name"
    input1_box = "name=>password"
    search_btn = "name=>submit"
    click_shangji = "link_text=>商机"
    #选中商机
    click_checkbox1="xpath=>//input[@value='23']"
    #编辑
    click_edit="xpath=>//input[@value='23']/../../td[13]/a[3]"
    def click_checkbox11(self):
        self.click(self.click_checkbox1)
        self.sleep(2)
    def click_edit1(self):
        self.click(self.click_edit)
        self.sleep(2)

    def type_input(self, in_text,in_text1):
        self.type(self.input_box, in_text)
        self.type(self.input1_box,in_text1)


    def send_submit_btn(self):
        self.click(self.search_btn)
        self.sleep(2)
    def click_shangji1(self):
        self.click(self.click_shangji)
        self.sleep(2)