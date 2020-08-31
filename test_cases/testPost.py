from test_cases.base import Base
import unittest

class TestPost(Base):

    def send_back(self,case_data):
        # 发送请求,判断响应
        res,expect_res = self.send_request(case_data)
        json_result = res.json()
        return self.assertEqual(expect_res,json_result['statusDesc'])

    def test_null_login(self):
        '''用户名密码为空的情况'''
        case_data = self.get_case_data('test_null_login')
        self.send_back(case_data)

    def test_wrongname_login(self):
        '''错误用户名登录'''
        case_data = self.get_case_data('test_wrongname_login')
        self.send_back(case_data)

    def test_wrongpwd_login(self):
        '''错误密码登录'''
        case_data = self.get_case_data('test_wrongpwd_login')
        self.send_back(case_data)

    def test_normal_login(self):
        '''正常登录'''
        case_data = self.get_case_data('test_normal_login')
        self.send_back(case_data)

if __name__ == "__main__":
     unittest.main()