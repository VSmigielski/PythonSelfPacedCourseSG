class extract:
    def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        while True:
            try:
                with open(file_path, encoding='utf-8', newline='') as f: 
                    csv_file = csv.DictReader(f, delimiter = delimiter,quotechar = quotechar) 
                    for row in csv_file:
                        dataset.append(row)
                return dataset
            except FileNotFoundError:
                print("The CSV file entered was not found! Please try again!")
                file_path = input("Enter a valid file path:\n") 
                if file_path != "quit":
                    continue
                else:
                    break
            else:
                print("That was a valid CSV file!")
                break
                
    def fromJSON(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
            
        import json
        
        dataset = list()
        
        while True:
            try:
                with open(file_path) as json_file:
                    data = json.load(json_file)
                    if type(data) is not list:
                        dataset.append(data)
                        return dataset
                    else:
                        return data
                    
            except (TypeError, ValueError) as e:
                print("The file could not be decoded")
                file_path = input("Enter a valid file path:\n")
                if file_path != "quit":
                    continue
                else:
                    break
            except FileNotFoundError:
                print("The JSON file entered was not found! Please try again!")
                file_path = input("Enter a valid file path:\n")
                if file_path != "quit":
                    continue
                else:
                    break
            else:
                return dataset
                break
    def fromExcel(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
            
        import xlrd
        
        while True:
            try:
                wb = xlrd.open_workbook(file_path)
                sheet = wb.sheet_by_index(0)
                sheet.cell_value(0, 0)

                keys = []
                for i in range(sheet.ncols):
                    keys.append(sheet.cell_value(0, i))
            
                dataset = []
            
                for i in range(1, sheet.nrows):
                    dic = dict()
                    for j in keys:
                        if j == "Date" and type(sheet.cell_value(i, keys.index(j))) is not str:
                            xl_date = sheet.cell_value(i, keys.index(j))

                            datetime_date = xlrd.xldate_as_datetime(xl_date, 0)
                            date_object = datetime_date.date()
                            string_date = date_object.isoformat()
                            dic[j] = string_date
                        else:
                            dic[j] = sheet.cell_value(i, keys.index(j))
                    dataset.append(dic)
                return dataset
                    
            except (TypeError, ValueError) as e:
                print("The file could not be decoded")
                file_path = input("Enter a valid file path:\n")
                if file_path != "quit":
                    continue
                else:
                    break
            except FileNotFoundError:
                print("The Excel file entered was not found! Please try again!")
                file_path = input("Enter a valid file path:\n")
                if file_path != "quit":
                    continue
                else:
                    break
            else:
                return dataset
                break