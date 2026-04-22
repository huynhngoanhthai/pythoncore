# danh sach chua ds
# 1 0 1 
# 1 1 1
# 1 1 1

# maTran = [
#     [1,0,1],
#     [1,1,1],
#     [1,1,1],
# ]

# ds1 = [1,2,3,4,5]

# ds1[2] # 3
# ds2 = list()

# print(len(ds1))
# print(ds2)

# in ra 
# print(ds1[len(ds1) - 1])


# ds = [1,2,3,4]
# a,b,c,d = ds

# tp = (1,2,3,4)

# print(len(tp))
# print(tp[-1])

# do tuple ko dc thay doi ne toc doc doc no se nhanh hon list

# *la phan con lai kieu list

# ds2 = [5,6,7,8]

# print(ds + ds2)

# ds.sort() / sap xep tang/giam
# ds.append(5) / them vao cuoi
# ds.clear() / xoa het cac phan tu
# ds.insert(2,1)
# ds.count(2)
# 1 ham có return 
# 2 là ham ko co return -> None
# print(ds.count(2))
# idx = ds.index(2)
# print(idx)
# ds.pop()# pop xoa phan tu thu index
# ds.remove(2) # pop xoa phan tu theo gia tri
# ds.reverse() # in nguoc lai

# ds2 = ds.copy()
# ds[2] = 10
# print(ds2 is ds)
# print(ds2)

# del ds[0]
# del ds

# ds.sort()
# ds2 = sorted(ds, reverse=False)
# ds = [8,2,9,4,2]

# sum(ds) tinh tong cac phan tu trong mang
# max(ds) tim max trong mang
# min(ds) tim min trong mang

# ds = [8,2,9,4,2]
# print()

# nhập vào năm và tháng in ra bao nhiu ngày
# 12-2020 
# 31

# 2020 % 4 == 0
# [31,28,,31,..,]
# n = input("nhap mm-yyyy: ")

# mm, yyyy = n.split("-")

# thang = [31,28,31,30,31,30,31,31,30,31,30,31]
# # True = 1, False = 0
# # True + 2 = 3
# print(thang[int(mm) - 1] + (int(yyyy) % 4 == 0 and int(mm) == 2))


# 10 đã có thế 10% 
# tiền góc là bào nhiu tiền thuế là bào nhiu 

#  n => 
# s = 1 + 2 + 3 + 4 + ... n
# n = 100 => 5050
# n = 10 => 55
# n = 4 => 10
# n = 3 => 6 


# (n + 1) * n /2 

# n = s
# (n + 1) - (n - 1) = 2 
# n((n + 1) - (n - 1)) = 2S
# n((n + 1)) - (n - 1).n = 2S
 
# 1.2 - 0.1
# 2.3 - 1.2
# 3.4 - 2.3

# n((n + 1)) / 2 