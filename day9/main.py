# câu điều kiện 

# syntax

# if dieukien:
    # max thuc thi


a = int(input("nhap a: "))

# if  a % 2 == 0:
#     print("la so chia het cho 2")


#  1
#  het

# 2 
# la so chia het cho 2
# het
# print("het")

# if  a % 2 == 0:
#     print("la so chan")
# else:
#     print("la so le")

# if  a % 2 == 0:
#     print("la so chan")
# elif a % 3 == 0:
#     print("la so le")


# if  a % 2 == 0:
#     print("la so chan")

# if a % 3 == 0:
#     print("la so le")

# if rut ron viet tren 1 dong duy nhat
#  gia_tri_dung if dieu_kien else gia_tri_sai  
# print("la so chan") if a % 2 == 0 else  print("la so le")

if a % 2 == 0 and a % 3 == 0:
    print("la so chia het cho 3 va 2")
ds = [1,2,3]

if a in ds:
    print("a co trong ds")

if a % 2 == 0 or a % 5 == 0:
    print("a chia het cho 5 hoac 2 ")

# toan thu khac

if a != 0 and a ==2:
    print("a khac 0")

if not (a == 0 or a == 2):
    print("a khac 0")