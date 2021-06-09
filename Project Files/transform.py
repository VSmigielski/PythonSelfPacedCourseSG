from extract import extract # import the external extract class
 
class transform:
    def head(self, dataset, step): #return the top N records from the dataset
        records = []
        records.append(dataset[:step])
        return records
    
    def tail(self, dataset, step): #return the last N records from the dataset
        records = []
        records.append(dataset[-step:])
        return records
    
    def rename_attribute(self, dataset, old, new): #rename a column in the dataset
        for row in dataset:
            if old in row.keys():
                row[new] = row.pop(old)
            else:
                pass
        return dataset
    
    def remove_attribute(self, dataset, del_col): #remove a column from the dataset
        for row in dataset:
            if del_col in row.keys():
                row.pop(del_col)
            else:
                pass
        return dataset
    
    def rename_attributes(self, dataset, old, new): #rename a list of columns in the dataset
        for row in dataset:
            for i in old:
                if i in row.keys():
                    index = old.index(i)
                    row[new[index]] = row.pop(old[index])
                else:
                    pass
        return dataset
    
    def remove_attributes(self, dataset, del_column): #remove a list of columns in the dataset
        for row in dataset:
            for i in del_column:
                if i in row.keys():
                    row.pop(i)
                else:
                    pass
        return dataset
    
    def transform(self):
        pass
    
    
e = extract()
dataset = e.fromCSV(file_path="citigroup.csv")
dataset2 = e.fromJSON(file_path="FileIO-DataFiles/prizes.json")

t = transform()

# recordsHead = t.head(dataset=dataset, step=5)
# recordsTail = t.tail(dataset=dataset, step=5)
# rename = t.rename_attribute(dataset=dataset, old="Date", new="Day of Year")
# delete = t.remove_attribute(dataset=dataset, del_col="Date")
# rename2 = t.rename_attributes(dataset=dataset, old=["Date", "High"], new=["Day of Year", "Maximum"])
# delete2 = t.remove_attributes(dataset=dataset, del_column=["Date", "High"])

# print(recordsHead)
# print("\n")
# print(recordsTail)
# print(rename)
# print(delete)
# print(rename2)
# print(delete2)