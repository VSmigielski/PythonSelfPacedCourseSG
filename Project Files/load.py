from extract import extract # import the external extract class
 
class load:
    def toCSV(self, file_path, dataset):
        import csv
        import os
        
        permission = "a"
        while True:
            try:
                if os.path.exists(file_path) == False:
                    permission = "w"
                else:
                    choice = input("Replace old data? (Y/N) ")
                    if choice.upper() == "Y":
                        permission = "w"
                        break
                    else:
                        choice = input("Append new data? (Y/N) ")
                        if choice.upper() == "Y":
                            permission = "a"
                            break
                        else:
                            raise FileExistsError
            
            except FileExistsError as e:
                print(file_path, "already exists! Please select a new file path: ")
                file_path = input("Enter a new valid CSV file path: ")
            
        with open(file_path, permission, newline='') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter = ",", fieldnames = dataset[0].keys())
            writer.writeheader()
            writer.writerows(dataset)
            
    def toJSON(self, file_path, dataset):
        import json
        import os
        
        permission = "a"
        while True:
            try:
                if os.path.exists(file_path) == False:
                    permission = "w"
                else:
                    choice = input("Replace old data? (Y/N) ")
                    if choice.upper() == "Y":
                        permission = "w"
                        break
                    else:
                        choice = input("Append new data? (Y/N) ")
                        if choice.upper() == "Y":
                            permission = "a"
                            break
                        else:
                            raise FileExistsError
            except FileExistsError as e:
                print(file_path, "already exists! Please select a new file path: ")
                file_path = input("Enter a new valid JSON file path: ")
                
        with open(file_path, permission) as json_file:
            if len(dataset) == 1:
                json.dump(dataset[0], json_file)
            else:
                json.dump(dataset, json_file)
                
    def toExcelXLS(self, dataset, file_path):
        import xlwt
        
        # Workbook is created
        wb = xlwt.Workbook()

        # add_sheet is used to create sheet.
        sheet1 = wb.add_sheet('Sheet 1')
        cnt = 0
        for key, value in dataset[0].items():
            sheet1.write(0, cnt, key)
            cnt += 1

        rowcnt = 1
        for data in dataset:
            cnt = 0
            for key, value in data.items():
                sheet1.write(rowcnt, cnt, value)
                cnt += 1
            rowcnt += 1
        wb.save(file_path)
    
    def toExcelXLSX(self, file_path, dataset):
        import os
        
        from datetime import datetime
        import xlsxwriter

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet()
        
        for row in dataset:
            keys = list(row.keys())
            
        values = list()
            
        for row in dataset:
            for k, v in row.items():
                values.append(v)
        
        col = 0
        
        for i in keys:
            worksheet.write(0, col, i)
            col += 1
        
        v_col = 0
        row = 1
        
        for i in values:
            if v_col == len(keys):
                row += 1
                v_col = 0
            worksheet.write(row, v_col, i)
            v_col += 1
        
        workbook.close()  
                
e = extract()
# dataset = e.fromCSV(file_path = 'citigroup.csv',delimiter = ',')
# dataset2 = e.fromJSON(file_path = 'FileIO-DataFiles/states-9.json')
# dataset3 = e.fromExcel(file_path='citigroup.xlsx')
dataset4 = e.fromExcel(file_path='citigroup.xlsx')
 
l = load()
# l.toCSV(file_path = "citigroup_copy.csv", dataset = dataset)
# l.toJSON(file_path = "FileIO-DataFiles/states-10.json", dataset = dataset2)
# l.toExcelXLS(file_path = "citigroup_copy.xlsx", dataset = dataset3)
l.toExcelXLSX(file_path = "citigroup_copy.xlsx", dataset = dataset4)