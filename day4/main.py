a = "Py"
b = 'Python'


# xin chao thai

# name = input()

# s = "XIN CHAO " + name

# mố số ký tự đặt biệt 
# \t => tag 
# \n => xuống hàng
# \\ => \
# \" => "
# \' => '


# a = " \"
# s = 'ten cong viet \' xay nen\''
# ten cong viet "xay nen"

# name = input("name: ")
# hour = input("hour: ")
# feature = input("feature: ")


# người a đang nhao vào hệ thông 
# ten: 
# giờ:
# chức năng
# content = "Người dùng a đang nhao vào hệ thông\nten:\t%s\ngio:\t%s\nchuc nang:\t%s"%(name,hour,feature) 
# print(content)
# %s => string
# %d => int
# %f => float
# %.2f => làm tròng đén số thử 2

# print("so: %.2f "%(12.23612))
# lib = 12
# print("thu vien: %s "%(lib))

# print('{} + {} = {}'.format(a, b, a+b))       # 4 + 3 = 7
# print('{} / {} = {:.2f}'.format(a, b, a/b))   # 4 / 3 = 1.33

# print('{} + {} = {} {} {} {} {}'.format(a, b, a+b)) 
# a = 4
# b = 3
# print(f"{a} + {b} = {a+b}")

# dãy ký tự 
# ngonNgu = "pyaa"
# a,b= ngonNgu

# print(a)
# print(b)

ngon_ngu = "jaVaScript hello youa"
# [start:chiều day:step]
# print(ngon_ngu[::-2]) # javas

# ham string 
# upper viet hoa
# lower
# capitalize
# title


# find => vi tri dau tien tien khi thay (tim, start, end) => neu ko -1
# rfind => vi tri cuoi cung (tim, start, end)=> neu ko -1
  
# index => vi tri dau tien tien khi thay (tim, start, end) => neu ko loi
# rindex => vi tri cuoi cung (tim, start, end) => neu ko loi
  
# count => dem so lương kí tự
# startswith => 
# endswith => 
# split => tách chuổi
# join => ghep chuổi
# strip => xoa khoanr trang

# ['jaVaScript','hello','youa']


# listTu = ngon_ngu.split(" ")
# 

# date = "2020-12-30"
# ['2020','12','30']
 
# print(date.split("-")[0])

# a = ['2020','12','30']
# 30/12/2020

# s = "hello hello a"
# s= s.replace("hello", "hi", -1)
# print(s)

# Phương Thức Kiểm Tra

# name = "2021"

# print(name.isalnum())

# 1
# HD0001
# 2
# HD0002

n = "12"
print(f"HD{n.rjust(4,'-')}")
# print(n.rjust(4,"-"))

