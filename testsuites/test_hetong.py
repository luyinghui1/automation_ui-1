from pageobjects.hetong_view import HomePage
from selenium import webdriver
import time
import unittest
from framework.browser_engine import BrowserEngine
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
        crmpage.click_hetong1()
        crmpage.click_checkbox11()
        crmpage.click_edit1()
    def tearDown(cls):
        print("here is end")
        cls.driver.quit()

    def test_abc(cls):
       print("abc")

if __name__ == '__main__':
    unittest.main()