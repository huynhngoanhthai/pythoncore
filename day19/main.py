# doc ghi file

# nếu read thì phải close()
# f = open("./a.py",'r')

# print(f.read())
# tự đóng file 
# with open("./text.txt","r") as f:
#     data = f.readlines()
#     # f.write("hello abc")
#     print(data)

# xoá 1 file

# import os

# if os.path.exists('./text.txt'):
#     os.remove('./text.txt')
# else:
#     print("khong co")

# loai file

# json object

import json

# person =  {
#     "name": "thai",
#     "age": 25,
#     "country": "VN"
# } 

# with open("data.json","w") as f:
#     json.dump(person, f)

# with open("data.json","r") as f:
#     # s = f.read()
#     # print(s)
#     # print(f.seek())
#     if f:
#         a = json.load(f)
#         print(type(a))
#         print(a)

# csv 
import csv

with open('data.csv', 'r') as f:
    # ds header
    csv_lines = csv.reader(f,delimiter=',') 
    line = 0
    for row in csv_lines:
        if line == 0:
            print(f"ten co: {' '.join(row)}")
        else: 
            print(f"hang: {' '.join(row)}")
        line+=1
        

# xlsx
# import xlrd
# excel = xlrd.open_workbook('./')
# # xlrd.open_workbook('/')
# print(excel.nsheets)
# print(excel.sheet_names())
