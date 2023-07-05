import os
import argparse
import csv

# Create Classes object 
class Class:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
# Create Students object
class Student: 
    def __init__(self, id, name, class_id, birthday, phonenb):
        self.id = id 
        self.name = name 
        self.class_id = class_id
        self.birthday = birthday
        self.phonenb = phonenb
        
# Create Teachers object
class Teacher: 
    def __init__(self, id, name, birthday, phonenb, hoc):
        self.id = id 
        self.name = name 
        self.birthday = birthday
        self.phonenb = phonenb
        self.hoc = hoc
        
# <--Class-->
def add_class(args):
    # Tạo đối tượng Class từ các tham số đầu vào
    new_class = Class(args.id, args.name)

    # Kiểm tra xem file classes.txt có tồn tại hay không
    if not os.path.exists('classes.txt'):
        # Nếu chưa tồn tại, tạo file mới với dòng đầu tiên là tên cột
        with open('classes.txt', 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['ID', 'Name'])

    # Ghi đối tượng Class vào file classes.txt
    with open('classes.txt', 'a', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow([new_class.id, new_class.name])
        
def edit_class(args):
    # Đọc dữ liệu từ file classes.txt vào một danh sách
    with open('classes.txt', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        rows = list(reader)

    # Tìm đối tượng classes cần chỉnh sửa trong danh sách
    found = False
    for row in rows[1:]:
        if int(row[0]) == args.id:
            row[1] = args.name
            found = True
            break

    # Nếu không tìm thấy đối tượng classes cần chỉnh sửa, báo lỗi và thoát
    if not found:
        print(f"Class with ID {args.id} not found.")
        return

    # Ghi lại danh sách Student vào file classes.txt
    with open('classes.txt', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerows(rows)    
        
def delete_class(args):
    # Đọc dữ liệu từ file students.txt vào một danh sách
    with open('classes.txt', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        rows = list(reader)

    # Tìm đối tượng Student cần xóa trong danh sách
    found = False
    for row in rows[1:]:
        if int(row[0]) == args.id:
            rows.remove(row)
            found = True
            break

    # Nếu không tìm thấy đối tượng Student cần xóa, báo lỗi và thoát
    if not found:
        print(f"Classes with ID {args.id} not found.")
        return

    # Ghi lại danh sách Student vào file students.txt
    with open('classes.txt', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerows(rows)  

# <--Students-->
def add_student(args):
    new_student = Student(args.id, args.name, args.class_id, args.birthday, args.phonenb)
    
    # Kiểm tra xem file classes.txt có tồn tại hay không
    if not os.path.exists('students.txt'):
        # Nếu chưa tồn tại, tạo file mới với dòng đầu tiên là tên cột
        with open('students.txt', 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['ID', 'Name', 'Class_ID', 'Birthday', 'Phone_Number'])

    # Ghi đối tượng Class vào file classes.txt
    with open('students.txt', 'a', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow([new_student.id, new_student.name, new_student.class_id, new_student.birthday, new_student.phonenb])
        
def edit_student(args):
    # Đọc dữ liệu từ file classes.txt vào một danh sách
    with open('students.txt', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        rows = list(reader)

    # Tìm đối tượng classes cần chỉnh sửa trong danh sách
    found = False
    for row in rows[1:]:
        if int(row[0]) == args.id:
            row[1] = args.name
            row[2] = args.class_id
            row[3] = args.birthday
            row[4] = args.phonenb
            found = True
            break

    # Nếu không tìm thấy đối tượng classes cần chỉnh sửa, báo lỗi và thoát
    if not found:
        print(f"Student with ID {args.id} not found.")
        return

    # Ghi lại danh sách Student vào file classes.txt
    with open('students.txt', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerows(rows) 
        
def delete_student(args):
    # Đọc dữ liệu từ file students.txt vào một danh sách
    with open('students.txt', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        rows = list(reader)

    # Tìm đối tượng Student cần xóa trong danh sách
    found = False
    for row in rows[1:]:
        if int(row[0]) == args.id:
            rows.remove(row)
            found = True
            break

    # Nếu không tìm thấy đối tượng Student cần xóa, báo lỗi và thoát
    if not found:
        print(f"Student with ID {args.id} not found.")
        return

    # Ghi lại danh sách Student vào file students.txt
    with open('students.txt', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerows(rows) 
        
# <--Teacher-->
def add_teacher(args):
    new_teacher = Teacher(args.id, args.name, args.birthday, args.phonenb, args.hoc)
    
    # Kiểm tra xem file classes.txt có tồn tại hay không
    if not os.path.exists('teachers.txt'):
        # Nếu chưa tồn tại, tạo file mới với dòng đầu tiên là tên cột
        with open('teachers.txt', 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['ID', 'Name', 'Birthday', 'Phone_Number', 'Head_of_Class'])

    # Ghi đối tượng Class vào file classes.txt
    with open('teachers.txt', 'a', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow([new_teacher.id, new_teacher.name, new_teacher.birthday, new_teacher.phonenb, new_teacher.hoc])
        
def edit_teacher(args):
    # Đọc dữ liệu từ file classes.txt vào một danh sách
    with open('teachers.txt', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        rows = list(reader)

    # Tìm đối tượng classes cần chỉnh sửa trong danh sách
    found = False
    for row in rows[1:]:
        if int(row[0]) == args.id:
            row[1] = args.name
            row[2] = args.birthday
            row[3] = args.phonenb
            row[4] = args.hoc
            found = True
            break

    # Nếu không tìm thấy đối tượng classes cần chỉnh sửa, báo lỗi và thoát
    if not found:
        print(f"Teacher with ID {args.id} not found.")
        return

    # Ghi lại danh sách Student vào file classes.txt
    with open('teachers.txt', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerows(rows) 
        
def delete_teacher(args):
    # Đọc dữ liệu từ file students.txt vào một danh sách
    with open('teachers.txt', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        rows = list(reader)

    # Tìm đối tượng Student cần xóa trong danh sách
    found = False
    for row in rows[1:]:
        if int(row[0]) == args.id:
            rows.remove(row)
            found = True
            break

    # Nếu không tìm thấy đối tượng Student cần xóa, báo lỗi và thoát
    if not found:
        print(f"Teacher with ID {args.id} not found.")
        return

    # Ghi lại danh sách Student vào file students.txt
    with open('teachers.txt', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerows(rows) 

if __name__ == '__main__':
    # Tạo đối tượng ArgumentParser tên là parser, biến này sẽ chứa và xử lý các tham số đầu vào từ CLI
    # ArgumentParser là một đối tượng trong module argparse của Python, được sử dụng để xử lý các tham số đầu vào từ dòng lệnh (command-line arguments).
    parser = argparse.ArgumentParser()
    # Khởi tạo đối tượng subparsers, add_parser() là 1 phương thức của đối tượng ArgumentParser, nó giúp tạo và quản lý các sub-parsers (lệnh con)
    subparsers = parser.add_subparsers()
    
    # <--Class-->
    # Khởi tạo đối tượng sub-parser tên là add_parser, tên này sẽ được sử dụng để chỉ định lệnh con cụ thể mà bạn muốn thực thi.
    add_parser = subparsers.add_parser('add_class')
    # Thêm đối số cho sub-parser với kiểu dữ liệu cụ thể
    add_parser.add_argument('--id', type=int, required=True)
    add_parser.add_argument('--name', type=str, required=True)
    # Set hàm mặc định khi sub-parser được thực hiện 
    add_parser.set_defaults(func=add_class)

    edit_parser = subparsers.add_parser('edit_class')
    edit_parser.add_argument('--id', type=int, required=True)
    edit_parser.add_argument('--name', type=str, required=True)
    edit_parser.set_defaults(func=edit_class)
    
    delete_parser = subparsers.add_parser('delete_class')
    delete_parser.add_argument('--id', type=int, required=True)
    delete_parser.set_defaults(func=delete_class)
    
    # <--Student-->
    add_parser = subparsers.add_parser('add_student')
    add_parser.add_argument('--id', type=int, required=True)
    add_parser.add_argument('--name', type=str, required=True)
    add_parser.add_argument('--birthday', type=str, required=True)
    add_parser.add_argument('--phonenb', type=int, required=True)
    add_parser.set_defaults(func=add_student)

    edit_parser = subparsers.add_parser('edit_student')
    edit_parser.add_argument('--id', type=int, required=True)
    edit_parser.add_argument('--name', type=str, required=True)
    edit_parser.add_argument('--birthday', type=str, required=True)
    edit_parser.add_argument('--phonenb', type=int, required=True)
    edit_parser.set_defaults(func=edit_student)
    
    edit_parser = subparsers.add_parser('delete_student')
    edit_parser.add_argument('--id', type=int, required=True)
    edit_parser.set_defaults(func=delete_student)

    # <--Teacher-->
    add_parser = subparsers.add_parser('add_teacher')
    add_parser.add_argument('--id', type=int, required=True)
    add_parser.add_argument('--name', type=str, required=True)
    add_parser.add_argument('--birthday', type=str, required=True)
    add_parser.add_argument('--phonenb', type=int, required=True)
    add_parser.add_argument('--hoc', type=str, required=True)
    add_parser.set_defaults(func=add_teacher)

    edit_parser = subparsers.add_parser('edit_teacher')
    edit_parser.add_argument('--id', type=int, required=True)
    edit_parser.add_argument('--name', type=str, required=True)
    edit_parser.add_argument('--birthday', type=str, required=True)
    edit_parser.add_argument('--phonenb', type=int, required=True)
    edit_parser.add_argument('--hoc', type=str, required=True)
    edit_parser.set_defaults(func=edit_teacher)
    
    edit_parser = subparsers.add_parser('delete_teacher')
    edit_parser.add_argument('--id', type=int, required=True)
    edit_parser.set_defaults(func=delete_teacher)   
    
    # Xử lý tham số đầu vào từ dòng lệnh
    # Khi sub-parser được gọi, các đối số (arguments) được truyền vào sẽ được lưu trữ trong đối tượng args được trả về bởi phương thức parse_args() của đối tượng ArgumentParser.
    # Sau khi các đối số được xác định và lưu trữ trong args, chúng ta có thể sử dụng thuộc tính của đối tượng args để truy cập các giá trị này. 
    # Cụ thể, chúng ta có thể sử dụng tên của đối số để truy cập giá trị tương ứng.
    args = parser.parse_args()
    # Gọi hàm được chỉ định cho một lệnh con, với các đối số của lệnh con đó được truyền vào qua đối tượng args.
    args.func(args)