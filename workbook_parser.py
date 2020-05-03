from translator import translate_from_hebrew
from columns_mapping import mapping, sheets_order

################################################
###constants###
################################################
FIRST_TABLE = None
NOT_ISRAEL_WORDS = ['מט"ח', 'חוץ לארץ', 'חו"ל']
ISRAEL_WORDS = ['ישראל', 'בארץ']
FIRST_FIELD_TABLE = ['שם נ"ע', 'שם המנפיק/שם נייר ערך']
MAX_METADATA_ROWS = 12
INCREMENT_SHEETS_COUNT = True
DONT_INCREMENT_SHEETS_COUNT = False


SHEETS_TO_SKIP = {
        # This is a sheet we expected and decided to increment the sheet iteration number.
        'סכום נכסי הקרן': INCREMENT_SHEETS_COUNT,
        # This is a sheet we did not expected and decided not to increment the iteration number.
        'Sheet1': DONT_INCREMENT_SHEETS_COUNT,
        # This is a sheet we did not expected and decided not to increment the iteration number.
        '{PL}PickLst': DONT_INCREMENT_SHEETS_COUNT,
        # This is a sheet we did not expected and decided not to increment the iteration number.
        'סקירת רוח מבקר': DONT_INCREMENT_SHEETS_COUNT,
        # This is a sheet we did not expected and decided not to increment the iteration number.
        'אישור רוח': DONT_INCREMENT_SHEETS_COUNT}


CELLS_TO_SKIP = ['* בעל ענין/צד קשור', 'בהתאם לשיטה שיושמה בדוח הכספי **','בעל ענין/צד קשור *']
################################################
###end of constants###
################################################


def get_cell(workbook,sheet_name, row, column):
    worksheet = workbook.sheet_by_name(sheet_name)
    cell = worksheet.cell(row,column).value
    return str(cell)


def get_entire_row(workbook, sheet_name, row, min_column=1, max_column=None):
    # return: row data :type: list
    row_data = []
    column = min_column
    
    # Get cell data.
    cell_data = get_cell(workbook, sheet_name, row, column)
    
    while should_iterate_columns(max_column, column, cell_data):
        row_data.append(cell_data)
        column += 1
        cell_data = get_cell(workbook, sheet_name, row, column)

    return row_data


def should_iterate_columns(max_column, column, cell_data):
    """
    If max column than use is_not_max_column lambda to check if is the max column. If max column is None, use
    data_exists lambda to check if cell data exists.
        
    :param max_column: Maximum columns we have.
    :param column: The current column indicator.
    :param cell_data: The data of the cell.
        
    :return: Rather we need to iterate over the current column or not.
    """
    if max_column:
        return not(max_column == column)

    if cell_data:
        return True

    return False


def parse_workbook(workbook, file_name):
    
    parsed_file = dict()
    
    # Not taking the index from self._workbook.sheet_names because there might be more sheets before the first one
    # we expecting. That's mean we need to keep track of the indexed by our self.
    sheet_index = 0
    
    sheet_names = workbook.sheet_names()
    
    for sheet_name in sheet_names:
        if sheet_name in SHEETS_TO_SKIP:
            # We need to skip this sheet or we got a sheet which not exists in the default sheet names.
            if SHEETS_TO_SKIP[sheet_name] == DONT_INCREMENT_SHEETS_COUNT:
                # The current sheet a sheet we don't want to iterate over but as we skipping it, we don't want
                # to increment the sheet index indicator. If we incremented then sheet at position 29, which is
                # OK, would consider 30 and that out of range of us.
                continue
            
            sheet_index = sheet_index + 1
            continue
            
        sheet_data = parse_sheet(sheet_name, sheet_index, workbook, file_name)
        #print("after parse sheet",sheet_name) #########################################33
        sheet_index = sheet_index + 1
        
        parsed_file[sheet_name] = sheet_data
        
    return parsed_file


def parse_sheet(sheet_name, sheet_index, workbook, file_name, start_row=0, start_column=1):
    """
    Parse excel pension report sheet.
        
    :param sheet_name: Sheet name
    :param sheet_index: The index of the sheet.
    :param start_row: Row number to start
    :param start_column: Column number to start
        
    :return: True / False
    """
    
    current_row = start_row
    current_column = start_column
    current_cell = None
    row_data = None
    
    worksheet = workbook.sheet_by_name(sheet_name)
        
    data = []
    sheet_metadata = {
        "Investment": sheet_name,
        "file_name": file_name
    }
    #print(sheet_metadata['file_name']) ######################################################******
    
    # Parse metadata, stop when find the first table field or until max metadata.
    start_metadata_row = current_row
    while current_cell not in FIRST_FIELD_TABLE:
        if current_cell:
            metadata = get_metadata(row_data) 
            #print("after get_metadata inside parse func", metadata)  ############################################  
            if metadata:
                translated_metadata = translate_from_hebrew(metadata[0]) 

                if translated_metadata:
                    metadata_field = translated_metadata
                else:
                    metadata_field = 'item_' + str({metadata[0]})

                sheet_metadata[metadata_field] = metadata[1]
                #print(sheet_metadata)  ###################################################################
                #print("")  ############################################
        current_row += 1
        row_data = get_entire_row(workbook, sheet_name, current_row, current_column,len(mapping[sheet_name.strip()])) # 11 is max col in cash, for each sheet we need to use its max col
        #print("after get_entire_row inside parse func",row_data)  ############################################
        
        if row_data:
            # Strip all spaces from start and end string.
            current_cell = row_data[0].strip()
        else:
            current_cell = None
            
        if current_row - start_metadata_row > MAX_METADATA_ROWS:
            print('Failed to parse sheet. There was no first column indicator for: ', file_name, sheet_name)
            return None
    ##############################################################
    # we got to  first table field!! now we will Get fields name #
    ##############################################################
    fields_len = len(get_entire_row(workbook, sheet_name, current_row, start_column,len(mapping[sheet_name.strip()]))) ################### change 11
    
    empty_len = 0
    current_cell = ""
    
    # Parsing until find the end of excel sheet.
    while current_cell not in CELLS_TO_SKIP:
        
        if empty_len > 5: ###################### why 5
            break
        
        current_row += 1
        if current_row == worksheet.nrows:
            break
        
        data_row = get_entire_row(workbook, sheet_name, current_row, start_column, fields_len + start_column)
        
        # Check if is empty row or first cell is empty then move to next iteration
        if not data_row or not data_row[0]:
            empty_len += 1
            continue
        
        current_cell = data_row[0]
        
        # if current cell start is a total row then parse it as a total row *** total row ***
        if current_cell.find('סה"כ') != -1:
            total_data, is_israel = parse_total_field(current_cell)
            #print("total_data & is_israel after parse_total_field:",total_data, is_israel) ###################################
            continue
        else:
            row = {
                "index": total_data,
                "israel": is_israel,
                "line_in_file": current_row
                }
            #print("after row total_data, is_israel, current_row:",total_data, is_israel,current_row) #########################
            
            for i in range(0, fields_len):
                key_in_mapping = i + 1
                if key_in_mapping not in mapping[sheets_order[sheet_index]]:
                    #print("There's no key",key_in_mapping,"in the mapping for",sheets_order[sheet_index]) ##############
                    continue
                row[mapping[sheets_order[sheet_index]][key_in_mapping]] = data_row[i]
            
            second_column_name = mapping[sheets_order[sheet_index]][2]
            
            if second_column_name in row and row[second_column_name]:
                # Add metadata and add row data to data list.
                row.update(sheet_metadata)
                data.append(row)
                
    #print() #################################            
    #print(data) ######################            
    return data


def get_metadata(data):
    """
    Parse metadata data.
    
    :param data: list of data
    """
    first_cell = data[0]
    
    if not first_cell:
        print("get_metadata: No data in first cell")
        return None, None
    
    finder = first_cell.find(":")
    # Find func return -1 when not find.
    if finder != -1:
        # Check if the colon char is not last data char (The meaning data in the first cell).
        if len(first_cell) > finder:
            return first_cell[:finder], first_cell[finder + 1:]
    # Check if len of data is bigger than one.
    elif len(data) > 1:
        return first_cell, data[1]


def parse_total_field(data):
    """
    Parse total field, total filed start with 'סה"כ' word in total field we get if the investment in Israel.
    """
    # strip 'סה"כ' word.
    total_data = data.strip('סה"כ')
    
    for iw in ISRAEL_WORDS:
        if total_data.find(iw) != -1:
            return total_data, True
    
    for niw in NOT_ISRAEL_WORDS:
        if total_data.find(niw) != -1:
            return total_data, False
    
    return total_data, True







