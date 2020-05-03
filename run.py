import os
from excel_handler import  excel_to_workbook
from workbook_parser import parse_workbook
from dict_to_json import from_dict_to_json

def main():
    directory = 'data/' # dir containing the excel files to parse
    for xlfile in os.listdir(directory):
        filename, workbook = excel_to_workbook(directory+xlfile)
        parsed_file = parse_workbook(workbook,filename)
        from_dict_to_json(parsed_file,filename)



if __name__ == "__main__":
    main()