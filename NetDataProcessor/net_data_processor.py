import pandas as pd
import numpy as np
import sys
sys.path.append('../')
import myenvvar
from bs4 import BeautifulSoup
import pymysql
import glob
from sqlalchemy import create_engine
import ntpath
import tag_lists

class NetDataProcessor:
    '''
    A class to handle all the processing of the 'Net Data' 
    '''
    def __init__(self):
        self.engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user=myenvvar.db_vars['user'],
                               pw=myenvvar.db_vars['password'],
                               db=myenvvar.db_vars['db']),encoding = 'utf8')

        self.db = pymysql.connect("localhost",myenvvar.db_vars['user'] ,myenvvar.db_vars['password'] ,myenvvar.db_vars['db'])
        self.cursor = self.db.cursor()

        self.pnet_files_folder = r"C:\Users\orenz\Desktop\op_db\NetData\pensyanet_maslul_clali"
        self.gnet_files_folder = r"C:\Users\orenz\Desktop\op_db\NetData\gemelnet_maslul_clali"

    def populate_pnet_general_table(self):
        # get existing files from db so we don't try to read them again
        self.cursor.execute('''select distinct file_name from pnet_general''')
      
        existing_file_names_list = [item[0] for item in list(self.cursor.fetchall())]

        existing_file_names_list_full_path = [r"{}\{}".format(self.pnet_files_folder,item) for item in existing_file_names_list]

        # list all pnet xml files in the directory
        all_files_list = glob.glob(r"{}\*.xml".format(self.pnet_files_folder))

        # new files to insert
        new_files_list = list(set(all_files_list) - set(existing_file_names_list_full_path))

        # tags list for pnet
        tagsList = tag_lists.tags_list_pnet
        
        # read and insert tables to db
        for file_ in new_files_list:
            with open(file_,'r',encoding='utf8') as file:
                handler = file.read()
                soup = BeautifulSoup(handler, features="html.parser")
            arr = []
            for tag in tagsList:
                temp_arr = [item.text for item in soup.find_all(tag)]
                # print(len(temp_arr)) to check if we have same amount of values for each tag
                arr.append(temp_arr)
            df = pd.DataFrame(np.array(arr).T,columns=tagsList)
            df['file_name'] = ntpath.basename(file_)
    
            # Insert whole DataFrame into MySQL
            df.to_sql('pnet_general', con = self.engine, if_exists = 'append',index=False)


    def populate_gnet_general_table(self):
        # get existing files from db so we don't try to read them again
        self.cursor.execute('''select distinct file_name from gnet_general''')
      
        existing_file_names_list = [item[0] for item in list(self.cursor.fetchall())]

        existing_file_names_list_full_path = [r"{}\{}".format(self.gnet_files_folder,item) for item in existing_file_names_list]

        # list all gnet xml files in the directory
        all_files_list = glob.glob(r"{}\*.xml".format(self.gnet_files_folder))

        # new files to insert
        new_files_list = list(set(all_files_list) - set(existing_file_names_list_full_path))

        # tags list for pnet
        tagsList = tag_lists.tags_list_gnet
        
        # read and insert tables to db
        for file_ in new_files_list:
            with open(file_,'r',encoding='utf8') as file:
                handler = file.read()
                soup = BeautifulSoup(handler, features="html.parser")
            rows = soup.find_all('row')
            rows_arr = []
            for row in rows:
                row_arr = []
                for tag in tagsList:
                    cell = row.find(tag)
                    if cell:
                        row_arr.append(cell.text)
                    else:
                        row_arr.append(cell)
    
            rows_arr.append(row_arr)
        
            df = pd.DataFrame(np.array(rows_arr), columns=tagsList)    
            df['file_name'] = ntpath.basename(file_)
    
            # Insert whole DataFrame into MySQL
            df.to_sql('gnet_general', con = self.engine, if_exists = 'append',index=False)




#################################################################################################################################
#################################################################################################################################

if __name__ == "__main__":

    netDataProcessor = NetDataProcessor()
    netDataProcessor.populate_pnet_general_table()
    netDataProcessor.populate_gnet_general_table()
    

