#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

wb = xlrd.open_workbook("test_user_data.xlsx")  # 打开excel
sh = wb.sheet_by_name("TestUserLogin")  # 按工作簿名定位工作表
print(sh.nrows)  # 有效数据行数
print(sh.ncols)  # 有效数据列数
print(sh.cell(0, 0).value)  # 输出第一行第一列的值`case_name`
print(sh.row_values(0))  # 输出第1行的所有值（列表格式）

# 将数据和标题组装成字典，使数据更清晰
print(dict(zip(sh.row_values(0), sh.row_values(1))))

# 遍历excel,打印所有的数据
for i in range(sh.nrows):
    print(sh.row_values(i))