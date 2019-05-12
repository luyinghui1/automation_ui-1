from pageobjects.hetong_view import HomePage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from framework.browser_engine import BrowserEngine
from selenium.webdriver.support import expected_conditions as EC
class Test_hetong_view(unittest.TestCase):
    def setUp(cls):
        browse = BrowserEngine(cls)
        cls.driver=browse.open_browser(cls)
        crmpage = HomePage(cls.driver)
        time.sleep(2)
        crmpage.type_input("admin", "123456")  #
        time.sleep(2)
        crmpage.send_submit_btn()
        time.sleep(2)
        crmpage.get_windows_img()
        #crmpage.click_hetong1()
        #crmpage.click_checkbox11()
        #crmpage.click_edit1()
    def tearDown(cls):
        print("here is end")
        cls.driver.quit()

    def test_abc(cls):
        cls.driver.find_element_by_link_text('合同').click()
        cls.driver.find_element_by_link_text('添加合同').click()
        cls.driver.find_element_by_name('business_name').click()
        time.sleep(2)
        cls.driver.find_element_by_css_selector("input[value='21']").click()

        # dr.find_element_by_xpath("//div[@id='dialog-message']/../div[3]/div/button[1]/span").click()


        cls.driver.find_element_by_xpath("//div[@id='dialog-business']/../div[3]/div/button[1]/span").click()
        time.sleep(2)
        cls.driver.find_element_by_id('due_time').click()
        time.sleep(2)
        #判断该frame是否可以切换进去，如果可以的话，返回True并且切换进去，否则返回False
        frame_is_available =EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@src,'about:blank')]"))

        cls.assertTrue(frame_is_available(cls.driver))
        #cls.driver.switch_to.frame(cls.driver.find_element_by_xpath("//iframe[contains(@src,'about:blank')]"))
        #cls.driver.find_element_by_css_selector("input[value='今天']").click()

if __name__ == '__main__':
    unittest.main()