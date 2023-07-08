import os 
import csv
import time

class dbQuery():
    def __init__(self):
        self.table_name = None
        self.list_conditions_columns = None 
        self.conditions_columns = None
        self.value = None
        self.data = None
        self.column_name = None
        self.rows = None
        self.indices = {}
      
    # <--method chaining-->
    # Select([ array of column names ]): Truyền vào tên các cột cần lấy data
    def select(self, list):
        self.list_conditions_columns = list
        return self
        
    # Where(column_name, value): Set điều kiện cần lọc ví dụ dbQuery.where(‘id', 1)
    def where(self, column_name, value):
        self.conditions_columns = column_name
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
        index_column = rows[0].index(self.conditions_columns)
        
        # thêm các row thỏa mãn giá trị value của phương thức where
        for row in rows[1:]:
            if str(row[index_column]) == str(self.value): 
                results.append(row)
                    
        columns_selected = []
        
        # lấy index của các columns từ phương thức select
        for field in self.list_conditions_columns:
            columns_selected.append(rows[0].index(field))

        results_last = []
        
        # lặp qua từng result là row thỏa mãn điều kiện where, sau đó chỉ lấy các giá trị thuộc columns từ phương thức select
        start_time = time.time()
        for result in results:
            new_list = [result[i] for i in range(len(result)) if i in columns_selected]
            results_last.append(new_list)
        end_time = time.time()
        
        
            
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
        index_column = rows[0].index(self.conditions_columns)
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
        index_column = rows[0].index(self.conditions_columns)
        for row in rows[1:]:
            if str(row[index_column]) == str(self.value): 
                # xóa row nếu thỏa mãn điều kiện where
                rows.remove(row)
                
        with open(self.table_name, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows)  
            
        return self   
    
    # Thêm method: create_index(table_name, column_name)
    def create_index(self, table_name, column_name):
        self.table_name = table_name
        self.column_name = column_name
         
        column_index = None
        
        with open(self.table_name, newline='') as f: 
            reader = csv.reader(f, delimiter='|')
            self.rows = list(reader)
            
        # Tìm column index 
        column_index = self.rows[0].index(self.column_name)
        
        if column_index is None: 
            raise ValueError(f"Column '{self.column_name}' not found in table '{self.table_name}'")

        # Sắp xếp các giá trị của cột theo thứ tự tăng dần
        sorted_rows = sorted(self.rows, key=lambda x: x[column_index])
        
        # Tạo cấu trúc dữ liệu cây nhị phân để lưu trữ các giá trị và vị trí của chúng trong bảng
        self.indices[self.column_name] = self._create_binary_tree(sorted_rows, 0, len(sorted_rows)-1, column_index)
        
    def _create_binary_tree(self, rows, start, end, column_index):
        # Kiểm tra điều kiện dừng
        if start > end:
            return None

        # Tìm giá trị trung bình và tạo node cây nhị phân mới
        mid = start + (end - start) // 2
        node = {"value": rows[mid][column_index], "index": mid}

        # Tạo các node con bên trái và bên phải
        node["left_child"] = self._create_binary_tree(rows, start, mid-1, column_index)
        node["right_child"] = self._create_binary_tree(rows, mid+1, end, column_index)

        return node

    def select_use_index(self, column_name, value):
        self.column_name = column_name
        self.value = value
        # Kiểm tra xem cột đã có index chưa
        if self.column_name not in self.indices:
            raise ValueError(f"Index on column '{self.column_name}' not found in table '{self.table_name}'")

        # Sử dụng cấu trúc dữ liệu cây nhị phân để tìm kiếm nhanh chóng giá trị cần tìm
        node = self.indices[self.column_name]
        while node is not None:
            if node["value"] == self.value:
                return self.rows[node["index"]]
            elif self.value < int(node["value"]):
                node = node["left_child"]
            else:
                node = node["right_child"]

        return None            
            
# Khởi tạo dbQuery object
dbquery = dbQuery()

# test get() method
# rs = dbquery.select(['ID', 'Name']).where('ID', 1).from_table('students.txt').get()

# test insert() method
# dbquery.insert(table_name='students.txt', data=[4, "Dong", "19062001", "126"])

# test time with index
# db_use_index = dbQuery()
# db_use_index.create_index(table_name='students_data.txt', column_name='ID')
# start_time = time.time()
# db_use_index.select_use_index(column_name='ID', value=669416)
# end_time = time.time()

# elapsed_time = end_time - start_time
    
# print(f"Thời gian tìm kiếm: {elapsed_time:.2f} giây")