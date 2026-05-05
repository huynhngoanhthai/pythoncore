# Hàm Bậc Cao
# co the nhan dc 1 hoac nhiu tham so
# tra ve ket qua cua ham khac
# co the chinh sua ham 
# ham co the gan 1 bien

# def sums_number(nums):
#     return sum(nums)

# def max_of_list(f,lst) :
#     func = f(lst)
#     return func

# def avg(nums):
#     return sum(nums)/len(nums) 

# print(max_of_list(avg, [1,2,3,4]))


# def square(x):
#     return x**2
# def cube(x) :
#     return x**3

# def calc(type):
#     if type == "square":
#         return square
#     elif type == "cube":
#         return cube
    

# result = calc("square")(2)
# print(result)


# result = calc("cube")(2)
# print(result)

# inner function

# def add_10():
#     ten = 10
#     def add(num):
#         return num + ten
    
#     return add

# # add(10)
# print(add_10()(10))

# ham hay dung

# map
# map(func, <tham_so>)

# ds = ['1','2',3,4,5]

# # def square(x):
# #     return x ** 2

# # ds2 = map(square,ds)
# ds2 = map(int,ds)


# print(list(ds2))

# filter
# filter(func, <tham_so>)

# ds = [{
#     "id": 1,
#     "name": "thai",
#     "isDeleted": True
# }, {
#     "id": 2,
#     "name": "thai2",
#     "isDeleted": False

#     # ...
# }, {
#     "id": 3,
#     "name": "thai3",
#     "isDeleted": False

#     # ...
# }]

# ds2 = filter(lambda i: i["isDeleted"] == False, ds)
# print(list(ds2))

# reduce
# reduce(func, <tham_so>)
# gia tri

# from functools import reduce
# ds = [1,2,3,4]

# total = reduce(lambda a,b: a * b, ds)

# print(total)