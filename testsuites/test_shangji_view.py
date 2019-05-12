#from pageobjects.shangji_view import HomePage

import time
import unittest
from selenium.webdriver.support import expected_conditions as EC

import ddt
import os


import sys

import os
print(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.getcwd()))
print(sys.path)

from pageobjects.shangji_view import HomePage
from readdata.read_excel import read_excel
from framework.logger import Logger

from framework.browser_engine import BrowserEngine
print(sys.path)
# create a logger instance
logger = Logger(logger="test_shangji_view").getlog()
file_path=os.path.dirname(os.path.abspath('.')) + '/testdata/testdata.xls';
excel = read_excel(file_path, 'Sheet2')
@ddt.ddt
class Test_shangji_view(unittest.TestCase):
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
        crmpage.click_shangji1()
        title_is_shangji = EC.title_is(u'ATesting CRM - Powered By 悟空CRM')
        cls.assertTrue(title_is_shangji(cls.driver))
        crmpage.click_checkbox11()
        crmpage.click_edit1()
    def tearDown(cls):
        print("here is end")
        cls.driver.quit()

    @ddt.data(*excel.next())
    def test_abc(cls,data):
        crmpage = HomePage(cls.driver)
        print(data['expect1'])
        try:
            assert data['expect1'] in crmpage.get_page_source()
            logger.info('Test Pass.')
            title_is_crm = EC.title_is("ATesting CRM - Powered By 悟空CRM")
            logger.info('Test Pass.%s',cls.assertTrue(title_is_crm(cls.driver)))
        except Exception as e:
            logger.error('Test Fail.'% e)



if __name__ == '__main__':
    unittest.main()





