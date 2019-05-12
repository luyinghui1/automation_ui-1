# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
import sys
sys.path.append(os.path.dirname(os.getcwd()))

# 设置报告文件保存路径


report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
#fp = file(HtmlFile, "wb")
#file_path = "F:\\RobotTest\\result.html"

# 构建suite
suite=unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_shangji_view.Test_shangji_view','test_title_contains.ALoginTest2','test_heng.Test_hetong_view']))
#suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_shangji_view))
file_result= open(HtmlFile, 'wb')
print(file_result)

if __name__ =='__main__':

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title=u"atest项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
    file_result.close()

