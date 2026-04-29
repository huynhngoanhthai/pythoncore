# 📘 Ngày 13 - List Comprehension & Hàm Lambda

## List Comprehension

List comprehension trong Python là cách tạo danh sách ngắn gọn từ một chuỗi (sequence). Đây là cú pháp rút gọn để tạo danh sách mới và nhanh hơn đáng kể so với dùng vòng lặp `for` thông thường.

```py
# Cú pháp
[biểu_thức for i in iterable if điều_kiện]
```

### Ví dụ 1: Chuyển chuỗi thành danh sách ký tự

```py
# Cách thông thường
language = 'Python'
lst = list(language)
print(type(lst))  # list
print(lst)        # ['P', 'y', 't', 'h', 'o', 'n']

# Dùng list comprehension
lst = [i for i in language]
print(type(lst))  # list
print(lst)        # ['P', 'y', 't', 'h', 'o', 'n']
```

### Ví dụ 2: Tạo danh sách số

```py
# Tạo số từ 0 đến 10
numbers = [i for i in range(11)]
print(numbers)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tính bình phương
squares = [i * i for i in range(11)]
print(squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Tạo danh sách tuple
numbers = [(i, i * i) for i in range(11)]
print(numbers)   # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), ...]
```

### Ví dụ 3: Kết hợp với điều kiện if

```py
# Lọc số chẵn
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Lọc số lẻ
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)   # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Lọc số chẵn dương từ danh sách
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)  # [4, 6, 8, 10]

# Làm phẳng mảng 2 chiều
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Hàm Lambda

Hàm lambda là hàm ẩn danh nhỏ gọn, không có tên. Nó có thể nhận bất kỳ số lượng tham số nào nhưng chỉ có một biểu thức. Hàm lambda tương tự anonymous function trong JavaScript — hữu ích khi cần viết hàm ẩn danh bên trong một hàm khác.

### Tạo Hàm Lambda

Dùng từ khóa `lambda`, theo sau là tham số và biểu thức. Hàm lambda không dùng `return` nhưng tự động trả về kết quả của biểu thức:

```py
# Cú pháp
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```

```py
# So sánh hàm thường vs lambda
def add_two_nums(a, b):
    return a + b
print(add_two_nums(2, 3))  # 5

# Chuyển thành lambda
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))  # 5

# Lambda tự gọi (self-invoking)
(lambda a, b: a + b)(2, 3)  # 5

square = lambda x: x ** 2
print(square(3))   # 9

cube = lambda x: x ** 3
print(cube(3))     # 27

# Nhiều biến
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))  # 22
```

### Hàm Lambda Bên Trong Hàm Khác

```py
def power(x):
    return lambda n: x ** n

cube = power(2)(3)           # cần 2 cặp ngoặc để gọi
print(cube)                  # 8

two_power_of_five = power(2)(5)
print(two_power_of_five)     # 32
```

## 💻 Bài Tập: Ngày 13

1. Dùng list comprehension lọc ra các số âm và số 0:
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   # kết quả: [-4, -3, -2, -1, 0]
   ```

2. Làm phẳng danh sách lồng nhau:
   ```py
   list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   # kết quả: [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

3. Dùng list comprehension tạo danh sách tuple theo mẫu:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (2, 1, 2, 4, 8, 16, 32),
    ...
    (10, 1, 10, 100, 1000, 10000, 100000)]
   ```

4. Làm phẳng danh sách countries và chuyển thành chữ hoa:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   # kết quả: [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```

5. Chuyển danh sách countries thành danh sách dictionary:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   # kết quả:
   # [{'country': 'FINLAND', 'city': 'HELSINKI'},
   #  {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   #  {'country': 'NORWAY', 'city': 'OSLO'}]
   ```

6. Chuyển danh sách names thành danh sách chuỗi ghép:
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   # kết quả: ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```

7. Viết hàm lambda giải phương trình hệ số góc (slope) hoặc giao điểm trục y (y-intercept) của hàm tuyến tính.

🎉 CHÚC MỪNG! 🎉
