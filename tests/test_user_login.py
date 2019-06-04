#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
import json
import requests
from lib.read_excel import *
from config.config import *
from lib.case_log import log_case_info
import os

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserLogin")

    def test_user_login_normal(self):
        case_data = get_test_data(self.data_list, "test_user_login_normal")
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, data=json.loads(data))
        log_case_info('test_user_login_normal', url, data, expect_res, res.text)
        self.assertEqual(res.text, expect_res)

    def test_user_login_password_wrong(self):
        case_data = get_test_data(self.data_list, 'test_user_login_password_wrong')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据

        res = requests.post(url=url, data=json.loads(data))
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.text, expect_res)  # 断言


