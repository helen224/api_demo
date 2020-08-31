from test_cases.base import Base
import unittest

class TestGet(Base):

    def send_back(self,case_data):
        # 发送请求,判断响应
        res,expect_res = self.send_request(case_data)
        json_result = res.json()
        return self.assertEqual(expect_res,json_result['message'])

    def test_get1(self):
        '''searchAuthor接口'''
        case_data = self.get_case_data('test_get')
        self.send_back(case_data)

    def test_get2(self):
        '''音乐排名接口'''
        case_data = self.get_case_data('test_getRanking1')
        self.send_back(case_data)

    def test_get3(self):
        '''音乐排名接口'''
        case_data = self.get_case_data('test_getRanking2')
        self.send_back(case_data)


if __name__ == "__main__":
    unittest.main()