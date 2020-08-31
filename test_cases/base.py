import unittest
import requests
import json
import sys
from common.read_excel import ExcelUtil
'''pip install requests'''
sys.path.append("../..")   # 统一将包的搜索路径提升到项目根目录下

class Base(unittest.TestCase):   # 继承unittest.TestCase

    # 读取Excel,根据类名（cls.__name__）读取Excel中对应Sheet的内容
    @classmethod
    def setUpClass(cls):
        if cls.__name__ != 'Base':
            sheet_name = cls.__name__
            cls.data_list = ExcelUtil.excel_to_list(cls,'../data/demodata.xls',sheet_name)

    # 获取数据
    def get_case_data(self, case_name):
        return ExcelUtil.get_test_data(self,self.data_list, case_name)

    # 发送请求,返回响应
    def send_request(self, case_data):
        url = case_data.get('url')
        args = case_data.get('args')
        headers = case_data.get('headers')
        expect_res = case_data.get('expect_result')
        method = case_data.get('method')
        data_type = case_data.get('data_type')
        if method.upper() == 'GET':   # GET类型请求
            res = requests.get(url=url)
        else:                          #POST请求
            res = requests.post(url=url, json=json.loads(args))   # JSON格式请求
        return res,expect_res