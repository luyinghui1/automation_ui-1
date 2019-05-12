from pageobjects.atest_login import HomePage
from selenium import webdriver
import time
import unittest
from framework.browser_engine import BrowserEngine
from selenium.webdriver.support import expected_conditions as EC
class ALoginTest(unittest.TestCase):
    def test_atesting_login(cls):
        #driver = webdriver.Firefox()
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        # driver=webdriver.Chrome()
        crmpage = HomePage(browse.driver)

        login_before = EC.title_is(u'员工登录 - Powered By 悟空CRM')
        cls.assertTrue(login_before(cls.driver))
        #cls.assertTure(login_before(cls.driver))
        login_before1 = EC.title_contains(u'员工登录')
        cls.assertTrue(login_before1(cls.driver))
        print("登陆前title断言成功")
        time.sleep(2)
        # driver=webdriver.Chrome()
        crmpage = HomePage(cls.driver)
        time.sleep(2)

        crmpage.type_input("admin", "123456")  # 调用页面对象中的方法
        # crmpage.type_input("123456")  # 调用页面对象中的方法
        time.sleep(2)
        crmpage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)

        login_after = EC.title_is(u'ATesting CRM - Powered By 悟空CRM')
        cls.assertTrue(login_after(cls.driver))
        login_after1 = EC.title_contains(u'ATesting CRM')
        cls.assertTrue(login_after1(cls.driver))
        print("登陆后title断言成功")

        crmpage.get_windows_img()  # 调用基类截图方法
        cls.driver.quit()