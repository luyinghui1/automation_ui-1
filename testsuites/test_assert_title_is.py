from pageobjects.atest_login import HomePage
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from framework.browser_engine import BrowserEngine
class ALoginTest1(unittest.TestCase):
    def test_atesting_login(cls):
        #driver=webdriver.Firefox()
        browse = BrowserEngine(cls)
        cls.driver=browse.open_browser(cls)

        time.sleep(3)
        title_is_before_login = EC.title_is('员工登录 - Powered By 悟空CRM')
        cls.assertTrue(title_is_before_login(cls.driver))
#driver=webdriver.Chrome()
        crmpage = HomePage(cls.driver)
        time.sleep(2)

        crmpage.type_input("admin","123456")  # 调用页面对象中的方法
#crmpage.type_input("123456")  # 调用页面对象中的方法
        time.sleep(2)
        crmpage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
       # 断言 title 是指定的内容
        title_is_before_login = EC.title_is(u'ATesting CRM - Powered By 悟空CRM')
        cls.assertTrue(title_is_before_login(cls.driver))
        crmpage.get_windows_img()  # 调用基类截图方法
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()