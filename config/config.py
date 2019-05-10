#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的绝对路径的上一级，__file__指当前文件

data_path = os.path.join(prj_path, 'data')  # 数据目录，暂时在项目目录下
test_path = prj_path  # 用例目录，暂时在项目目录下

log_file = os.path.join(prj_path, 'log', 'log.txt')  # 也可以每天生成新的日志文件
report_file = os.path.join(prj_path, 'report', 'report.html')  # 也可以每次生成新的报告

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式


# 数据库配置
db_host = '115.28.108.130'   # 自己的服务器地址
db_port = 3306
db_user = 'test'
db_passwd = '123456'
db = 'api_test'

# 邮件配置
smtp_server = 'smtp.sina.com'
smtp_user = 'test_results@sina.com'
smtp_password = 'hanzhichao123'

sender = smtp_user  # 发件人
receiver = '851025859@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题


