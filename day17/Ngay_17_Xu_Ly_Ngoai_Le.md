# 📘 Ngày 17 - Xử Lý Ngoại Lệ (Exception Handling)

## Xử Lý Ngoại Lệ

Python dùng `try` và `except` để xử lý lỗi một cách "mềm mại" (gracefully). Xử lý lỗi nhẹ nhàng nghĩa là chương trình phát hiện lỗi nghiêm trọng và thoát ra một cách có kiểm soát, thường kèm thông báo mô tả lỗi, giúp ứng dụng không bị crash.

```py
try:
    # code chạy khi mọi thứ ổn
except:
    # code chạy khi có lỗi xảy ra
```

```py
try:
    print(10 + '5')
except:
    print('Có lỗi xảy ra')
```

### Xử Lý Nhiều Loại Lỗi

```py
try:
    name = input('Nhập tên của bạn:')
    year_born = input('Năm sinh của bạn:')
    age = 2019 - int(year_born)
    print(f'Bạn là {name}. Bạn {age} tuổi.')
except TypeError:
    print('Lỗi kiểu dữ liệu (TypeError)')
except ValueError:
    print('Lỗi giá trị (ValueError)')
except ZeroDivisionError:
    print('Lỗi chia cho không (ZeroDivisionError)')
else:
    print('Khối else chạy khi không có lỗi')
finally:
    print('Khối finally luôn luôn chạy')
```

```sh
Nhập tên của bạn: Asabeneh
Năm sinh của bạn: 1920
Bạn là Asabeneh. Bạn 99 tuổi.
Khối else chạy khi không có lỗi
Khối finally luôn luôn chạy
```

### Dùng Exception as e (Rút Gọn)

```py
try:
    name = input('Nhập tên của bạn:')
    year_born = input('Năm sinh:')
    age = 2019 - int(year_born)
    print(f'Bạn là {name}. Bạn {age} tuổi.')
except Exception as e:
    print(e)
```

## Đóng Gói và Giải Nén Tham Số (Packing & Unpacking)

Python dùng hai toán tử:
- `*` cho tuple
- `**` cho dictionary

### Giải Nén (Unpacking)

#### Giải Nén Danh Sách

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]

# Không dùng unpacking → lỗi
# print(sum_of_five_nums(lst))  # TypeError

# Dùng * để giải nén
print(sum_of_five_nums(*lst))  # 15
```

```py
# Giải nén trong range()
args = [2, 7]
numbers = range(*args)
print(list(numbers))  # [2, 3, 4, 5, 6]
```

```py
# Giải nén một phần
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)    # 1 [2, 3, 4, 5, 6] 7
```

#### Giải Nén Dictionary

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} sống ở {country}, {city}. {age} tuổi.'

dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
print(unpacking_person_info(**dct))
# Asabeneh sống ở Finland, Helsinki. 250 tuổi.
```

### Đóng Gói (Packing)

Dùng khi không biết trước số lượng tham số:

#### Đóng Gói Danh Sách

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1, 2, 3))              # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### Đóng Gói Dictionary

```py
def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))
```

```sh
name = Asabeneh
country = Finland
city = Helsinki
age = 250
```

## Spread (Trải Rộng) Trong Python

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

## Enumerate

Dùng `enumerate` khi cần cả chỉ số lẫn giá trị khi lặp:

```py
for index, item in enumerate([20, 30, 40]):
    print(index, item)
# 0 20
# 1 30
# 2 40
```

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'Quốc gia {i} được tìm thấy tại index {index}')
# Quốc gia Finland được tìm thấy tại index 0
```

## Zip

Dùng `zip` để kết hợp nhiều danh sách khi lặp:

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

print(fruits_and_veges)
# [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, ...]
```

## 💻 Bài Tập: Ngày 17

1. Cho danh sách: `names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']`
   - Giải nén 5 quốc gia đầu tiên vào biến `nordic_countries`
   - Lưu Estonia vào biến `es` và Russia vào biến `ru`

🎉 CHÚC MỪNG! 🎉
