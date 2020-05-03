import openpyxl
import xlrd
import os

def excel_to_workbook(file_path):
    path , extension = os.path.splitext(file_path)
    filename = path.split('/')[-1]
    if extension.lower() == '.xls':
        workbook = xlrd.open_workbook(filename=file_path)
    return filename, workbook