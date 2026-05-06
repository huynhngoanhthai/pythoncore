# 📘 Ngày 21 - Lớp và Đối Tượng (Classes and Objects)

## Lớp và Đối Tượng là gì?

Python là ngôn ngữ lập trình hướng đối tượng. Mọi thứ trong Python đều là đối tượng — số, chuỗi, danh sách, dictionary, tuple, set đều là đối tượng của class tương ứng. Ta tạo class để tạo đối tượng. Class giống như một bản thiết kế (blueprint) để tạo ra các đối tượng.

Kiểm tra mọi thứ trong Python đều là class:

```py
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

## Tạo một Class

Dùng từ khóa `class` theo sau là tên và dấu hai chấm. Tên class phải theo kiểu **CamelCase**:

```py
# Cú pháp
class ClassName:
    code here

# Ví dụ
class Person:
    pass

print(Person)  # <class '__main__.Person'>
```

## Tạo một Đối Tượng

Gọi class như một hàm để tạo đối tượng:

```py
p = Person()
print(p)  # <__main__.Person object at 0x10804e510>
```

## Constructor (Hàm Khởi Tạo)

Python có hàm khởi tạo `__init__()`. Tham số `self` là tham chiếu đến instance hiện tại của class:

```py
class Person:
    def __init__(self, name):
        self.name = name  # gắn tham số vào class

p = Person('Asabeneh')
print(p.name)  # Asabeneh
```

Thêm nhiều tham số:

```py
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)  # Asabeneh
print(p.age)        # 250
print(p.country)    # Finland
```

## Phương Thức Của Đối Tượng

Đối tượng có thể có các phương thức (method) — tức là các hàm thuộc về đối tượng:

```py
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} {self.age} tuổi. Sống ở {self.city}, {self.country}.'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
# Asabeneh Yetayeh 250 tuổi. Sống ở Helsinki, Finland.
```

## Giá Trị Mặc Định Cho Tham Số

Đặt giá trị mặc định để tránh lỗi khi tạo đối tượng mà không truyền tham số:

```py
class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} {self.age} tuổi. Sống ở {self.city}, {self.country}.'

p1 = Person()  # dùng giá trị mặc định
print(p1.person_info())
# Asabeneh Yetayeh 250 tuổi. Sống ở Helsinki, Finland.

p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
# John Doe 30 tuổi. Sống ở Noman city, Nomanland.
```

## Phương Thức Chỉnh Sửa Giá Trị

Thêm phương thức để chỉnh sửa thuộc tính của đối tượng:

```py
class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} {self.age} tuổi. Sống ở {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
print(p1.skills)  # ['HTML', 'CSS', 'JavaScript']

p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.skills)  # []
```

## Kế Thừa (Inheritance)

Kế thừa cho phép tái sử dụng code của class cha. Class con kế thừa tất cả phương thức và thuộc tính từ class cha:

```py
class Student(Person):
    pass  # kế thừa toàn bộ từ Person

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')

print(s1.person_info())
# Eyob Yetayeh 30 tuổi. Sống ở Helsinki, Finland.

s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)  # ['JavaScript', 'React', 'Python']

print(s2.person_info())
s2.add_skill('Marketing')
print(s2.skills)  # ['Marketing']
```

## Ghi Đè Phương Thức Của Class Cha

Ta có thể ghi đè (override) phương thức của class cha bằng cách định nghĩa lại phương thức cùng tên trong class con. Dùng `super()` để gọi constructor của class cha:

```py
class Student(Person):
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250,
                 country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = 'Anh ấy' if self.gender == 'male' else 'Cô ấy'
        return f'{self.firstname} {self.lastname} {self.age} tuổi. {gender} sống ở {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')

print(s1.person_info())
# Eyob Yetayeh 30 tuổi. Anh ấy sống ở Helsinki, Finland.

s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)  # ['JavaScript', 'React', 'Python']

print(s2.person_info())
# Lidiya Teklemariam 28 tuổi. Cô ấy sống ở Espoo, Finland.

s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)  # ['Marketing', 'Digital Marketing']
```

> **Lưu ý:** Khi thêm `__init__()` trong class con, nó sẽ không còn tự động kế thừa `__init__()` từ class cha nữa. Ta cần gọi `super().__init__()` để truy cập các thuộc tính của class cha.

## 💻 Bài Tập: Ngày 21

### Bài tập cấp độ 1

1. Tạo class `Statistics` với các phương thức tính toán thống kê trên một mảng số:

```py
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
print('Số lượng:', data.count())    # 25
print('Tổng:', data.sum())          # 744
print('Min:', data.min())           # 24
print('Max:', data.max())           # 38
print('Khoảng:', data.range())      # 14
print('Trung bình:', data.mean())   # 30
print('Trung vị:', data.median())   # 29
print('Yếu vị:', data.mode())       # (26, 5)
print('Phương sai:', data.var())    # 17.5
print('Độ lệch chuẩn:', data.std()) # 4.2
print('Phân phối tần suất:', data.freq_dist())
# [(20.0, 26), (16.0, 27), (12.0, 32), ...]
```

### Bài tập cấp độ 2

1. Tạo class `PersonAccount` với các thuộc tính: `firstname`, `lastname`, `incomes` (danh sách thu nhập kèm mô tả), `expenses` (danh sách chi tiêu kèm mô tả). Class cần có các phương thức:
   - `total_income()` — tổng thu nhập
   - `total_expense()` — tổng chi tiêu
   - `account_info()` — thông tin tài khoản
   - `add_income(amount, description)` — thêm khoản thu
   - `add_expense(amount, description)` — thêm khoản chi
   - `account_balance()` — số dư (thu - chi)

🎉 CHÚC MỪNG! 🎉
