import unittest,time,os
from common.HTMLTestRunner import HTMLTestRunner
from test_cases.testGet import TestGet
from test_cases.testPost import TestPost

'''复制文件BeautifulReport，至python安装Lib\site-packages位置下'''
from BeautifulReport import BeautifulReport

if __name__ == "__main__":
    '''指定文件路径生成测试报告'''
    report_dir='./reports'
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_name='\\'+now+' test_report.html'
    ftp = open(report_name, 'wb')

    '''建立一个测试用例集'''
    suite = unittest.TestSuite()
    suite.addTest(TestGet("test_get1"))
    suite.addTest(TestGet("test_get2"))
    suite.addTest(TestGet("test_get3"))
    suite.addTest(TestPost("test_null_login"))
    suite.addTest(TestPost("test_wrongname_login"))
    suite.addTest(TestPost("test_wrongpwd_login"))
    suite.addTest(TestPost("test_normal_login"))

    # '''运行用例集生成报告 --- HTMLTestRunner'''
    # runner = HTMLTestRunner(stream=ftp, title='接口测试', description='get、post接口测试',tester="Emma Liu")
    # runner.run(suite)


    '''运行用例集生成报告 --- BeautifulReport'''
    result = BeautifulReport(suite)
    result.report(description='接口测试', filename= report_name, log_path=report_dir)