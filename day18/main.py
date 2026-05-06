# regex 
# thư viện đung để xử lý chuổi kí tự

import re

# hàm match() dùm để tìm kiếm đầu chuổi 

# text = "hello, toi la thai"

# match = re.match('hea',text)
# print(match)
# 
# span = match.span()
# print(span[0], span[1])

# code = "HD10012"
# code2 = "HD20012"

# match = re.match('HD1',code2)

# py2 in 
# print()

# search()
# text = "hello, thai toi la thai"
# # se tim kiêm cum ký tư đầu tiền cho biết vị trí
# match = re.search('thai',text)

# print(match)


# # hello, thai toi la thai => [thai, thai]

# # findall
# match = re.findall(',',text)
# print(match) 20

# sub thay thể ký từ 

# text = "hello, thai toi la thai"

# match = re.sub('thai','thanh',text)

# print(match)

# match = re.split(" ", text)

# print(match)

# mẫu RegEx

# t = re.findall(r"[]", text)
# print(t)
# []  trong khoản [a-z] 
# A-z lấy tất cả từ ko kệ viêt hoá học thường


# t = re.findall(r"[0-9]+", text)
# t = re.findall(r"e.", text)
# t = re.findall(r"[A-z]+|[0-9]+", text)
# t = re.findall(r"[A-z]+", text) + re.findall(r"[0-9]+", text)
# t = re.findall(r"e.+", text)
# t = re.findall(r"[a-z].*", text)



# t = re.findall(r"[0-9]{2}", text)  +re.findall(r"[0-9]{4}", text)
# ngay thang dd/mm/yyyy hoac dd-mm-yyyy 
# in ra ds các ngay thang năm 
text = "happy new year26, happy 2029, email e-mail 20/12/2020 1 999, á 22-12-1998"

t = re.findall(r"[0-9]{2}-?/?[0-9]{2}-?/?[0-9]{4}", text)
# t = re.findall(r"[0-9]{2}-?/?[0-9]{2}-?/?[0-9]{4}", text)

t = re.findall(r"[A-z0-9]+", text)




print(t)