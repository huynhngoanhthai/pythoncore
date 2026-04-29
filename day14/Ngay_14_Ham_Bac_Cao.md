# 📘 Ngày 14 - Hàm Bậc Cao (Higher Order Functions)

## Hàm Bậc Cao là gì?

Trong Python, hàm được coi là "công dân hạng nhất" (first-class citizen), cho phép thực hiện các thao tác sau:

- Hàm có thể nhận một hoặc nhiều hàm khác làm tham số
- Hàm có thể được trả về như kết quả của hàm khác
- Hàm có thể được chỉnh sửa
- Hàm có thể được gán cho một biến

## Hàm Là Tham Số

```py
def sum_numbers(nums):  # hàm thông thường
    return sum(nums)

def higher_order_function(f, lst):  # hàm nhận hàm khác làm tham số
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # 15
```

## Hàm Là Giá Trị Trả Về

```py
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):  # hàm bậc cao trả về hàm khác
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))   # 9
result = higher_order_function('cube')
print(result(3))   # 27
result = higher_order_function('absolute')
print(result(-3))  # 3
```

## Closure trong Python

Python cho phép hàm lồng bên trong truy cập phạm vi của hàm bao ngoài — đây gọi là **Closure**. Closure được tạo bằng cách lồng một hàm bên trong hàm khác rồi trả về hàm bên trong đó.

```py
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))   # 15
print(closure_result(10))  # 20
```

## Decorator trong Python

Decorator là một mẫu thiết kế (design pattern) cho phép thêm chức năng mới vào một đối tượng hiện có mà không thay đổi cấu trúc của nó. Decorator thường được gọi trước khi định nghĩa hàm cần trang trí.

### Tạo Decorator

Để tạo decorator, ta cần một hàm bên ngoài chứa một hàm wrapper bên trong:

```py
# Hàm thông thường
def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g())  # WELCOME TO PYTHON

# Dùng cú pháp @ (decorator)
@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting())  # WELCOME TO PYTHON
```

### Áp Dụng Nhiều Decorator Lên Một Hàm

```py
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

# Decorator được thực thi từ dưới lên trên
@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting())  # ['WELCOME', 'TO', 'PYTHON']
```

### Decorator Nhận Tham Số

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("Tôi sống ở {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("Tôi là {} {}. Tôi thích dạy học.".format(first_name, last_name))

print_full_name("Asabeneh", "Yetayeh", "Finland")
```

## Các Hàm Bậc Cao Có Sẵn (Built-in)

### Hàm map()

Hàm `map()` nhận một hàm và một iterable làm tham số, áp dụng hàm đó lên từng phần tử:

```py
# Cú pháp
map(function, iterable)
```

```py
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

# Dùng lambda
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]
```

```py
# Chuyển đổi kiểu dữ liệu
numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))  # [1, 2, 3, 4, 5]
```

```py
# Chuyển tên thành chữ hoa
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

### Hàm filter()

Hàm `filter()` gọi hàm chỉ định — hàm này trả về True/False — để lọc các phần tử thỏa điều kiện:

```py
# Cú pháp
filter(function, iterable)
```

```py
# Lọc số chẵn
numbers = [1, 2, 3, 4, 5]

def is_even(num):
    return num % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # [2, 4]
```

```py
# Lọc số lẻ
def is_odd(num):
    return num % 2 != 0

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # [1, 3, 5]
```

```py
# Lọc tên dài hơn 7 ký tự
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def is_name_long(name):
    return len(name) > 7

long_names = filter(is_name_long, names)
print(list(long_names))  # ['Asabeneh']
```

### Hàm reduce()

Hàm `reduce()` được định nghĩa trong module `functools`. Nó nhận hai tham số (hàm và iterable) nhưng trả về một giá trị duy nhất thay vì một iterable:

```py
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']

def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)  # 15
```

## 💻 Bài Tập: Ngày 14

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Bài tập cấp độ 1

1. Giải thích sự khác biệt giữa map, filter và reduce.
2. Giải thích sự khác biệt giữa hàm bậc cao, closure và decorator.
3. Định nghĩa một hàm gọi (call function) trước map, filter hoặc reduce rồi dùng chúng.
4. Dùng vòng lặp for để in từng quốc gia trong danh sách countries.
5. Dùng for để in từng tên trong danh sách names.
6. Dùng for để in từng số trong danh sách numbers.

### Bài tập cấp độ 2

1. Dùng map để chuyển tất cả quốc gia sang chữ hoa.
2. Dùng map để tạo danh sách bình phương của mỗi số trong numbers.
3. Dùng map để chuyển tất cả tên sang chữ hoa.
4. Dùng filter để lọc các quốc gia có chứa chữ 'land'.
5. Dùng filter để lọc các quốc gia có đúng 6 ký tự.
6. Dùng filter để lọc các quốc gia có 6 ký tự trở lên.
7. Dùng filter để lọc các quốc gia bắt đầu bằng chữ 'E'.
8. Kết hợp nhiều iterator (ví dụ: map → filter → reduce).
9. Khai báo hàm `get_string_lists` nhận một list và trả về list chỉ chứa các phần tử kiểu string.
10. Dùng reduce để tính tổng tất cả các số trong numbers.
11. Dùng reduce để ghép tất cả quốc gia thành câu: "Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries".
12. Khai báo hàm `categorize_countries` trả về danh sách quốc gia có cùng mẫu (ví dụ: 'land', 'ia', 'island', 'stan').
13. Tạo hàm trả về dictionary, trong đó key là chữ cái đầu của tên quốc gia, value là số lượng quốc gia bắt đầu bằng chữ cái đó.
14. Khai báo hàm `get_first_ten_countries` trả về 10 quốc gia đầu tiên.
15. Khai báo hàm `get_last_ten_countries` trả về 10 quốc gia cuối cùng.

### Bài tập cấp độ 3

1. Dùng file countries_data.py và thực hiện các nhiệm vụ sau:
   - Sắp xếp quốc gia theo tên, theo thủ đô, theo dân số.
   - Lọc ra 10 ngôn ngữ được nói nhiều nhất theo vị trí địa lý.
   - Lọc ra 10 quốc gia đông dân nhất.

🎉 CHÚC MỪNG! 🎉
