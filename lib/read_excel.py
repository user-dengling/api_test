#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import os
def excel_to_list(data_file, sheet):
    data_list = []  # 新建个空列表，来乘装所有的数据
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    header = sh.row_values(0)
    for i in range(1, sh.nrows):
        d = dict(zip(header, sh.row_values(i)))
        data_list.append(d)
    return data_list

def get_test_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data

if __name__ == '__main__':
    prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级
    print(prj_path)
    print(os.path.abspath(__file__))
 
    data_path = os.path.join(prj_path, 'data')

    data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserReg")
    cast_data = get_test_data(data_list, "test_user_reg_exist")
    print(cast_data)


# wb = xlrd.open_workbook("test_user_data.xlsx")
# sh = wb.sheet_by_name("TestUserLogin")
# print(sh.nrows)  # 有效数据行数
# print(sh.ncols)  # 有效数据列数
# print(sh.cell(0, 0).value)  # 输出第一行第一列的值`case_name`
# print(sh.row_values(0))  # 输出第1行的所有值（列表格式）
#
# # 将数据和标题组装成字典，使数据更清晰
# print(dict(zip(sh.row_values(0), sh.row_values(1))))
#
# # 遍历excel,打印所有的数据
# for i in range(sh.nrows):
#     print(sh.row_values(i))
