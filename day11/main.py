# syntax
# def ten_ham():
#     # code

# def welcome():
#     print("welcome 0")
#     print("welcome 1")
#     print("welcome 2")
#     print("welcome 3")


# welcome()

# welcome()

# def add(a,b):
#     return a + b


# print(add(5,8))

# ham co tham tra ve
# def add(a,b):
#     return a + b

# ham ko co tham tra ve 
# def welcome():
#     print("welcome 0")

# print(welcome())


# đệ quy
# def welcome(i = 0):
#     if i == 1: 
#         return
    
#     print("welcome 0")
#     i+=1
#     welcome(i)

# welcome(1)


# set thu tu tham so

# def info(ten = None,tuoi = None,noi_o = None, nam_sinh= None):
#     return {
#         "name":ten,
#         "tuoi":tuoi,
#         "noi_o":noi_o,
#         "nam_sinh":nam_sinh,
#     }

# print(info("thai",70,"hcm","2000"))
# print(info(ten="thai", tuoi=70, noi_o="hcm", nam_sinh="2000"))

# sum()

# sum(1,2,3) # 6
# sum(5,2,3) # 10
# sum(5,2,3,5) # 15
# sum(5,2,3,5,9) # 24

# ham co so luong tham so tuy y 
# def sum(*nums):
#     print(nums)
#     print(type(nums))

#     s =0
#     for num in nums:
#         if str(num).isdigit():
#             s += int(num)
#     print(s)


# sum(1,2,"a",3)


# def sumqq(pre: int,*nums: int):
#     print(nums)
#     print(type(nums))

#     s =0
#     for num in nums:
#         if str(num).isdigit():
#             s += int(num) + pre
#     return s

# print(sumqq(1,2, 4, 5))