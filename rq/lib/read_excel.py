#coding=utf-8
import xlrd

def excel_to_find(file_name,sheet):
    file_list=[]
    wb=xlrd.open_workbook(file_name)
    sh=wb.sheet_by_name(sheet)
    header=sh.row_values(0)
    for i in range(1,sh.nrows):
        d=dict(zip(header,sh.row_values(i)))
        file_list.append(d)

    return file_list

def get_excel_to(file_list,case_name):
    for case_data in file_list:
        if case_name==case_data['case_name']:
            return case_data






