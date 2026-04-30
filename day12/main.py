# co 2 file python 
# muôn 2 file này giao tiếp với nhau 
# module 

# import day12.module.mymodule as mymodule

# print(mymodule.add(2,3))

# import os,sys
# # print(os.path.dirname(os.path.abspath(__file__)))
# # print(os.path)

# path = os.path.abspath("/home/anhthai/Documents")

# if path not in sys.path:
#     sys.path.insert(0,path)

# import main

# main.welcome()

# import os
# tạo folder
# os.mkdir('test')
# print(os.getcwd())

# xoá folder
# os.rmdir('test')

# python3 main.py 3 4 
# 7

# import sys

# print(int(sys.argv[1]) + int(sys.argv[2]))

# a= input()
# b= input()

# lay 4 ham trong module
# from statistics import mean,median,mode,stdev # 4GB
# import statistics # 30GB

# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
# print(mean(ages))    # ~22.9  (trung bình)
# print(median(ages))  # 23     (trung vị)
# print(mode(ages))    # 20     (yếu vị)
# print(stdev(ages))   # ~2.3   (độ lệch chuẩn)

# # lay nguyen module

# # ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

# print(statistics.mean(ages))    # ~22.9  (trung bình)
# print(statistics.median(ages))  # 23     (trung vị)
# print(statistics.mode(ages))    # 20     (yếu vị)
# print(statistics.stdev(ages))   # ~2.3   (độ lệch chuẩn)

# from math import *
# from math import pi as PI, pow as mu, sqrt as can

# import math as toan_hoc
# print(mu(2,2))
# print(PI)
# print(can(4))

# print(toan_hoc.sqrt(6))

import random as ngau_nhien

# print(ngau_nhien.random()) # 0 -> 0.99999
# print(ngau_nhien.randint(1,100)) 
# choi lo to 

# 1 -> 90
# bóc tửng số sao cho dược 5 sô đã chọn 
# 10 
# .. 
# 10 33 50 66 88

# ds sô đã xuất hiện

# if random in ds 
# random
# else ds.append(random)


# ds số (1,90)
# (1,2,3, ... 90)
# boc so 3 - 1
# (1,2,90 ... 89,3)
# boc so 2 - 2 (90 - 2)
# (1,89,90 ... 2,3)

ds = list(range(1,91))
so_lan_boc = 0 

for i in range(5):
    # 0 -> 89
    vi_tri_boc = ngau_nhien.randint(0,90 - so_lan_boc - 1)
    
    print(ds[vi_tri_boc])

    temp = ds[vi_tri_boc] 
    ds[vi_tri_boc] = ds[90 - so_lan_boc - 1]
    ds[90 - so_lan_boc - 1] = temp
    so_lan_boc += 1

# password manh là password có ký tự không lập lại độ dai là 8 ký tự
# RT21:ak(