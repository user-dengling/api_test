import xlrd
import os



def excel_to_list(data_file, sheet ):
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    # header = sh.row_values(0)

    return sh




if __name__ == '__main__':
    prj_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(prj_path, 'data')
    sh = excel_to_list(os.path.join(data_path, 'test_user_data.xlsx'), 'TestUserLogin')
    print(sh.row_values(0))
    print(sh.nrows)
    print(sh.ncols)