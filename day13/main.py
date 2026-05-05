# List Comprehension

# 0,1,2,3,4
# 0,2,4,6,8

# [<gia tri tra ve> for <bien> in <ds> ]

# ds = [0,1,2,3,4]

# ds2 = [ i*2 for i in ds]

# print(ds2)

# ds = [{
#     "id":1,
#     "name": "thai"
#     # ...
# },{
#     "id":2,
#     "name": "thai2"
#     # ...
# },{
#     "id":3,
#     "name": "thai3"
#     # ...
# }]

# # ds ten
# ds2 = [ i["id"] for i in ds]

# print(ds2)

# ds = [
#     [1,0,0],
#     [1,1,0],
#     [1,1,1]
# ]

# ds2 = [ value for list in ds for value in list]

# print(ds2)

# ds = [0, 1, 2, 3, 4]
# # 0,2,4

# ds2 = [i for i in ds if i % 2 == 0]

# print(ds2)

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

# chỉ láy phân tư 

# ds2 = [i["id"] for i in ds if not i["isDeleted"] and i["id"] < 3 ]

# print(ds2)

# ham Lambda

# Lambda nghi la ham nhu no ko co ten va return lai 1 gia tri
# def add(a,b) 
#   return a + b

# lambda <bien1,bien2,...>: <tra ve>

# add = (lambda a,b: a + b) 
# print(add(2,3))

# def pow(x):
#     return lambda n: x ** n

# print(pow(2)(3))