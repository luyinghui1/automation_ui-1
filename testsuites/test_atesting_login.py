# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
import ddt
import os
from readdata.read_excel import read_excel
file_path=os.path.dirname(os.path.abspath('.')) + '/testdata/testdata.xlsx'
excel = read_excel(file_path, 'Sheet1')
@ddt.ddt
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    @ddt.data(*excel.next())
    def test_atesting_login(self,data):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        time.sleep(2)
        baidupage = HomePage(self.driver)
        time.sleep(2)
        baidupage.type_input(data['input']) # 调用页面对象中的方法
        time.sleep(2)
        baidupage.send_submit_btn()   #调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        baidupage.get_windows_img()  # 调用基类截图方法
        try:
            assert data['expect'] in HomePage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()



