# syntax
# try: 
    # code
# except: 
    # code



# try:
#     import math
#     math.PI 
#     a = int(input("nhap a "))
#     print(10/a)
# except Exception as e:
#     print("loi roi", e)

# dong goi va gian nen tham so
# * : rai so kieu tuple
# **: nen kieu tu dien

# def sum_3(a,b,c):
#     return a + b + c

# ds = [1,2,3]

# print(sum_3(*ds))

# args = [2,7]

# print()

# def in_info(name, tuoi):
#     return f"ten: {name} tuoi: {tuoi}"

# nguoi =  {
#     "name": "thai",
#     "tuoi" : 25
# }

# print(in_info(**nguoi))

# def sum (*num):
#     s = 0
#     for i in num:
#         s += i

#     return s

# print(sum(1,2,4))
# print(sum(4))

# def in_info(**kwargs):

#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#     return  kwargs

# in_info(name = "thai", tuoi = 12)

# ds = [1,2]
# ds3 = [0, *ds,*ds2]

# print(ds3)
# ds = [1,2]
# ds2 = [4,5,7,8] 
# ds3 = [10] 


# for index,item in enumerate(ds2):
#     print(index, item)

# for a,b,c in zip(ds,ds2,ds3):
#     print(a,b,c)