# toan tu co ban
# print(1 + 2)
# print(1 - 2)
# print(1 * 2)
# print(1 / 2)
# cmt bam "ctrl + /"
# 2 ** la binh phuong so muc 
# print(2 ** 4)
# ctrl + space

# chia lay phan du (%) 
print(10 % 3) # 1

# chia lay nguyen (//)
print(10 // 3) # 3

"""
day la cmt nhiu dong
"""
# if 3 > 5:
#     print("3 lon hon 5")
# else:
#     print("ket thuc")

# a = 1 #inter
# print(type(a))
# a = 3.14 #float
# print(type(a))

#  kieu dua lieu string

s = "huynh ngo anh thai"
s = 'thai'
s = '''
119 binh long,
binh hung hoa,
tp hcm
'''

# kieu bool 0/1 false/true
# print(3 > 5)
# print(3 < 5)
# print(3 == 5)
# print(3 != 5)
# dau bang = ma tinh cach la gan du lieu == la so sach

# print( False and True )
# print( True or True )
# 1 and 0, 0 and 1, 1 and 1 , 0 and 0
a = True
b = True
# print(a and b) # True
# print( not (a and b)) # False
# print( a or b) # true

# print( (not (a and b)) and (a or b) ) # False

# ds list
# duoc khai bao "[]"

# a = [1,2,3,4,"chu", True]
# print(a[-1])

# dang tu dien dc khai bao boi dau ngoac nhon {}
a = {
    'ho': 'Nguyen',
    'ten': 'Van An',
    'quoc_gia': 'Viet Nam',
    'tuoi': 25,
    'da_lap_gia_dinh': False,
    'ky_nang': ['Python', 'JavaScript', 'SQL']
}

# print(a['ho'],a['ten'], a['tuoi'])

#  tuple ()
a = (1,2,3,4) # tuple
b = [1,2,3,4] # array

b[0] = 10
# print(b)


# print(a)

# tap hop set 
a = {4,1,2,3,3} # 1,2,3 
print(type(a))

# 1. co a=5 b=10 tinh trung binh cong
# in ra ket qua trung binh cong

# 2. co n kiem tra xem no co chia het cho 7 hay khong
# true/false

# 3. cho vao 1 nam in ra nam no la nam con gi 
# 2001 -> ran 
# 2000 -> rong

# 12 0,1,2,3,4,5,6,7,8,9,10,11
trans = {
    8: 'rong',
    9: 'ran',
    10: 'ngua',
    11: 'de',
    0: 'khi',
    1: 'ga',
    2: 'cho',
    3: 'heo',
    4: 'chuot',
    5: 'trau',
    6: 'ho',
    7: 'meo'
}
print(2001 % 12)
print(trans[2000 % 12]) 
