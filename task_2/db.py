import os 
import csv

class dbQuery():
    def __init__(self):
        self.table_name = None
        self.list_columns_name = None 
        self.columns_name = None
        self.value = None
        self.data = None 
      
    # <--method chaining-->
    # Select([ array of column names ]): Truyền vào tên các cột cần lấy data
    def select(self, list):
        self.list_columns_name = list
        return self
        
    # Where(column_name, value): Set điều kiện cần lọc ví dụ dbQuery.where(‘id', 1)
    def where(self, column_name, value):
        self.columns_name = column_name
        self.value = value
        return self
        
    # From( table_name): Chọn entity cần lấy dữ liệu
    def from_table(self, table_name):
        self.table_name = table_name
        return self
        
    # Trả về dữ liệu
    def get(self):
        # Đọc file 
        with open(self.table_name, newline='') as f: 
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)
            
        results = []
        # lấy index của column_name được truyền vào 
        index_column = rows[0].index(self.columns_name)
        
        # thêm các row thỏa mãn giá trị value của phương thức where
        for row in rows[1:]:
            if str(row[index_column]) == str(self.value): 
                results.append(row)
                    
        columns_selected = []
        # lấy index của các columns từ phương thức select
        for field in self.list_columns_name:
            columns_selected.append(rows[0].index(field))

        results_last = []
        
        # lặp qua từng result là row thỏa mãn điều kiện where, sau đó chỉ lấy các giá trị thuộc columns từ phương thức select
        for result in results:
            new_list = [result[i] for i in range(len(result)) if i in columns_selected]
            results_last.append(new_list)
            
        return results_last
    
    # Insert(table_name, data): Thêm dữ liệu vào entity 
    def insert(self, table_name, data):
        self.table_name = table_name
        self.data = data 
        
        with open(self.table_name, newline='') as f: 
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)
            
            # kiểm tra độ dài của data có bằng độ dài của row không
            if len(rows[0]) != len(self.data):
                print("Error with data length")
            else: 
                # nếu thỏa mãn thì chèn data vào dòng cuối
                with open(self.table_name, 'a', newline='') as f: 
                    writer = csv.writer(f, delimiter='|')
                    writer.writerow(self.data)                
        
    # Update(table_name, data): Update dữ liệu (cần dùng hàm where() ở trên để set điều kiện)
    def update(self, table_name, data):
        self.table_name = table_name
        self.data = data
        
        with open(self.table_name, newline='') as f: 
            reader = csv.reader(f, delimiter='|')
            rows = list(reader) 
        
        # lấy index của column thỏa mãn phương thức where     
        index_column = rows[0].index(self.columns_name)
        for index, row in enumerate(rows[1:], start=1):
            if str(row[index_column]) == str(self.value): 
                # thay row thỏa mãn phương thức where bằng data
                rows[index] = self.data              

        # cập nhập lại file
        with open(self.table_name, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows) 
        
    # Delete(table_name): Delete  (cần dùng hàm where() ở trên để set điều kiện)
    def delete(self, table_name):
        self.table_name = table_name
        
        with open(self.table_name, newline='') as f: 
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)

        # lấy index của column thỏa mãn điều kiện where
        index_column = rows[0].index(self.columns_name)
        for row in rows[1:]:
            if str(row[index_column]) == str(self.value): 
                # xóa row nếu thỏa mãn điều kiện where
                rows.remove(row)
                
        with open(self.table_name, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows)  
            
        return self        
            
# Khởi tạo dbQuery object
dbquery = dbQuery()

# test get() method
# rs= dbquery.select(['ID', 'Name']).where('ID', 1).from_table('students.txt').get()

# test insert() method
# dbquery.insert(table_name='students.txt', data=[4, "Dong", "19062001", "126"])

# test update() method
# dbquery.where(column_name='ID', value=2).update(table_name='students.txt', data=["3", "Dat", "24122000", "126"])

# test detele() method
# dbquery.where(column_name='ID', value=1).delete('students.txt')