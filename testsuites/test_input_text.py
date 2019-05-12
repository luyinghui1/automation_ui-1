import sys
#print(sys.path)
import os
dirs=os.path.dirname(os.path.abspath('.'))
#print(os.path.dirname(os.getcwd()))
print(dirs)
#sys.path.append('/pageobjects/framework')
sys.path.append(dirs+'\pageobjects')
print(sys.path)
from atest_login import HomePage
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(dirs+'\\framework')
print(sys.path)
from browser_engine import BrowserEngine
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
class ALoginTest2(unittest.TestCase):
    def test_atesting_login(cls):
        #driver=webdriver.Firefox()
        browse = BrowserEngine(cls)
        cls.driver=browse.open_browser(cls)

        time.sleep(3)

        crmpage = HomePage(cls.driver)
        time.sleep(2)
        # 判断某个元素中的值属性是否包含预期的字符串
       # text_to_be_present_in_element_value = EC.text_to_be_present_in_element_value((By.NAME, 'submit'), '查询')
        crmpage.type_input("admin","123456")  # 调用页面对象中的方法
#crmpage.type_input("123456")  # 调用页面对象中的方法
        time.sleep(2)
        crmpage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        #locator=(By.   , 值）
        #EC.visibility_of_element_located(locator)

        locator = (By.LINK_TEXT, '日志动态')
        search_text_field_should_present = EC.visibility_of_element_located(locator)
        cls.assertTrue(search_text_field_should_present(cls.driver))

        ''' 动态等待10s，如果10s内element加载完成则继续执行下面的代码，否则抛出异常 '''
        #判断某个元素是否被加到了dom树里，并不代表该元素一定可见
        WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located(locator))
        #判断某个元素是否可见。可见代表元素非隐藏，并且元素的宽和高都不等于0
        WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located(locator))
        #cls.assertTrue(search_text_field_should_present(cls.driver))
        #判断某个元素是否可见
        aa = EC.visibility_of(cls.driver.find_element_by_name("search"))
        cls.assertTrue(aa(cls.driver))
        #判断某个元素中的文本是否包含了预期的字符串
        text_should_present = EC.text_to_be_present_in_element((By.ID, 'searchBtn'), '查询')
        cls.assertTrue(text_should_present(cls.driver))

        crmpage.get_windows_img()  # 调用基类截图方法
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()