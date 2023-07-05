import os
import argparse
import csv

# Create Classes object 
class Class:
    def __init__(self):
        self.class_name = None
        self.id = None
        self.name = None
        
        # <--Class-->
    def add_class(self, id, name, class_name):
        # Tạo đối tượng Class từ các tham số đầu vào
        self.id = id 
        self.name = name
        self.class_name = class_name

        # Kiểm tra xem file classes.txt có tồn tại hay không
        if not os.path.exists(str(self.class_name) + '.txt'):
            # Nếu chưa tồn tại, tạo file mới với dòng đầu tiên là tên cột
            with open(str(self.class_name) + '.txt', 'w', newline='') as f:
                writer = csv.writer(f, delimiter='|')
                writer.writerow(['ID', 'Name'])

        # Ghi đối tượng Class vào file classes.txt
        with open(str(self.class_name) + '.txt', 'a', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow([self.id, self.name])
        
    def edit_class(self, id, name):
        self.id = id
        self.name = name
        # Đọc dữ liệu từ file classes.txt vào một danh sách
        with open(str(self.class_name) + '.txt', newline='') as f:
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)

        # Tìm đối tượng classes cần chỉnh sửa trong danh sách
        found = False
        for row in rows[1:]:
            if int(row[0]) == self.id:
                row[1] = self.name
                found = True
                break

        # Nếu không tìm thấy đối tượng classes cần chỉnh sửa, báo lỗi và thoát
        if not found:
            print(f"Class with ID {self.id} not found.")
            return

        # Ghi lại danh sách Student vào file classes.txt
        with open(str(self.class_name) + '.txt', 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows)    
        
    def delete_class(self, id):
        self.id = id
        # Đọc dữ liệu từ file students.txt vào một danh sách
        with open(str(self.class_name) + '.txt', newline='') as f:
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)

        # Tìm đối tượng Student cần xóa trong danh sách
        found = False
        for row in rows[1:]:
            if int(row[0]) == self.id:
                rows.remove(row)
                found = True
                break

        # Nếu không tìm thấy đối tượng Student cần xóa, báo lỗi và thoát
        if not found:
            print(f"Classes with ID {self.id} not found.")
            return

        # Ghi lại danh sách Student vào file students.txt
        with open(str(self.class_name) + '.txt', 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows)  
        
# Create Students object
class Student: 
    def __init__(self):
        self.id = None 
        self.name = None 
        self.class_id = None
        self.birthday = None
        self.phonenb = None
        
    # <--Students-->
    def add_student(self, id, name, class_id, birthday, phonenb):
        self.id = id 
        self.name = name 
        self.class_id = class_id
        self.birthday = birthday
        self.phonenb = phonenb        
        # Kiểm tra xem file classes.txt có tồn tại hay không
        if not os.path.exists(self.class_id + '.txt'):
            # Nếu chưa tồn tại, tạo file mới với dòng đầu tiên là tên cột
            with open(self.class_id + '.txt', 'w', newline='') as f:
                writer = csv.writer(f, delimiter='|')
                writer.writerow(['ID', 'Name', 'Class_ID', 'Birthday', 'Phone_Number'])

        # Ghi đối tượng Class vào file classes.txt
        with open(self.class_id + '.txt', 'a', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow([self.id, self.name, self.class_id, self.birthday, self.phonenb])
        
    def edit_student(self, id, name, class_id, birthday, phonenb):
        self.id = id 
        self.name = name 
        self.class_id = class_id
        self.birthday = birthday
        self.phonenb = phonenb  
        # Đọc dữ liệu từ file classes.txt vào một danh sách
        with open(self.class_id + '.txt', newline='') as f:
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)

        # Tìm đối tượng classes cần chỉnh sửa trong danh sách
        found = False
        for row in rows[1:]:
            if int(row[0]) == self.id:
                row[1] = self.name
                row[2] = self.class_id
                row[3] = self.birthday
                row[4] = self.phonenb
                found = True
                break

        # Nếu không tìm thấy đối tượng classes cần chỉnh sửa, báo lỗi và thoát
        if not found:
            print(f"Student with ID {self.id} not found.")
            return

        # Ghi lại danh sách Student vào file classes.txt
        with open(self.class_id + '.txt', 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows) 
            
    def delete_student(self, id):
        self.id = id
        # Đọc dữ liệu từ file students.txt vào một danh sách
        with open(self.class_id + '.txt', newline='') as f:
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)

        # Tìm đối tượng Student cần xóa trong danh sách
        found = False
        for row in rows[1:]:
            if int(row[0]) == self.id:
                rows.remove(row)
                found = True
                break

        # Nếu không tìm thấy đối tượng Student cần xóa, báo lỗi và thoát
        if not found:
            print(f"Student with ID {self.id} not found.")
            return

        # Ghi lại danh sách Student vào file students.txt
        with open(self.class_id + '.txt', 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows) 
            
# Create Teachers object
class Teacher: 
    def __init__(self):
        self.id = None 
        self.name = None 
        self.birthday = None
        self.phonenb = None
        self.hoc = None
        
    # <--Students-->
    def add_teacher(self, id, name, birthday, phonenb, hoc):
        self.id = id 
        self.name = name 
        self.birthday = birthday
        self.phonenb = phonenb    
        self.hoc = hoc    
        # Kiểm tra xem file classes.txt có tồn tại hay không
        if not os.path.exists('teachers.txt'):
            # Nếu chưa tồn tại, tạo file mới với dòng đầu tiên là tên cột
            with open('teachers.txt', 'w', newline='') as f:
                writer = csv.writer(f, delimiter='|')
                writer.writerow(['ID', 'Name', 'Birthday', 'Phone_Number', 'HoC'])

        # Ghi đối tượng Class vào file classes.txt
        with open('teachers.txt', 'a', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow([self.id, self.name, self.birthday, self.phonenb, self.hoc])
        
    def edit_teacher(self, id, name, birthday, phonenb, hoc):
        self.id = id 
        self.name = name 
        self.birthday = birthday
        self.phonenb = phonenb 
        self.hoc = hoc 
        # Đọc dữ liệu từ file classes.txt vào một danh sách
        with open('teachers.txt', newline='') as f:
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)

        # Tìm đối tượng classes cần chỉnh sửa trong danh sách
        found = False
        for row in rows[1:]:
            if int(row[0]) == self.id:
                row[1] = self.name
                row[2] = self.birthday
                row[3] = self.phonenb
                row[4] = self.hoc
                found = True
                break

        # Nếu không tìm thấy đối tượng classes cần chỉnh sửa, báo lỗi và thoát
        if not found:
            print(f"Teacher with ID {self.id} not found.")
            return

        # Ghi lại danh sách Student vào file classes.txt
        with open('teachers.txt', 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows) 
            
    def delete_teacher(self, id):
        self.id = id
        # Đọc dữ liệu từ file students.txt vào một danh sách
        with open('teachers.txt', newline='') as f:
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)

        # Tìm đối tượng Student cần xóa trong danh sách
        found = False
        for row in rows[1:]:
            if int(row[0]) == self.id:
                rows.remove(row)
                found = True
                break

        # Nếu không tìm thấy đối tượng Student cần xóa, báo lỗi và thoát
        if not found:
            print(f"Student with ID {self.id} not found.")
            return

        # Ghi lại danh sách Student vào file students.txt
        with open('teachers.txt', 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows) 