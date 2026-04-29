# 📘 Ngày 15 - Các Loại Lỗi Trong Python (Python Error Types)

## Tổng Quan

Khi viết code, việc mắc lỗi đánh máy hay các lỗi phổ biến khác là điều bình thường. Nếu code không chạy được, trình thông dịch Python sẽ hiển thị thông báo lỗi cho biết vị trí xảy ra vấn đề và loại lỗi. Hiểu các loại lỗi sẽ giúp bạn debug nhanh hơn và trở thành lập trình viên giỏi hơn.

## SyntaxError (Lỗi Cú Pháp)

Xảy ra khi code vi phạm quy tắc cú pháp của Python.

```py
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?

# Sửa lỗi:
>>> print('hello world')
hello world
```

## NameError (Lỗi Tên)

Xảy ra khi sử dụng một biến hoặc tên chưa được khai báo.

```py
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined

# Sửa lỗi: khai báo biến trước khi dùng
>>> age = 25
>>> print(age)
25
```

## IndexError (Lỗi Chỉ Số)

Xảy ra khi truy cập vào chỉ số (index) nằm ngoài phạm vi của danh sách.

```py
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

Danh sách chỉ có index từ 0 đến 4, nên index 5 là ngoài phạm vi.

## ModuleNotFoundError (Lỗi Không Tìm Thấy Module)

Xảy ra khi nhập một module không tồn tại.

```py
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'

# Sửa lỗi: dùng đúng tên module
>>> import math
```

## AttributeError (Lỗi Thuộc Tính)

Xảy ra khi truy cập vào thuộc tính hoặc phương thức không tồn tại trong đối tượng/module.

```py
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'

# Sửa lỗi: dùng đúng tên thuộc tính (chữ thường)
>>> math.pi
3.141592653589793
```

## KeyError (Lỗi Khóa)

Xảy ra khi truy cập một key không tồn tại trong dictionary.

```py
>>> users = {'name': 'Asab', 'age': 250, 'country': 'Finland'}
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'

# Sửa lỗi: dùng đúng tên key
>>> users['country']
'Finland'
```

## TypeError (Lỗi Kiểu Dữ Liệu)

Xảy ra khi thực hiện phép toán trên các kiểu dữ liệu không tương thích.

```py
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Sửa lỗi: chuyển đổi kiểu dữ liệu
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
```

## ImportError (Lỗi Import)

Xảy ra khi không thể nhập một hàm cụ thể từ module.

```py
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'

# Sửa lỗi: dùng đúng tên hàm
>>> from math import pow
>>> pow(2, 3)
8.0
```

## ValueError (Lỗi Giá Trị)

Xảy ra khi hàm nhận được đối số có kiểu đúng nhưng giá trị không hợp lệ.

```py
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
```

Không thể chuyển chuỗi '12a' thành số vì có ký tự 'a'.

## ZeroDivisionError (Lỗi Chia Cho Không)

Xảy ra khi thực hiện phép chia cho số 0.

```py
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Không thể chia một số cho 0.

---

> 💡 **Mẹo:** Đọc hiểu thông báo lỗi là kỹ năng quan trọng giúp bạn debug nhanh hơn. Hãy chú ý đến tên loại lỗi và dòng thông báo để biết chính xác vấn đề xảy ra ở đâu.

## 💻 Bài Tập: Ngày 15

1. Mở Python interactive shell và thử tất cả các ví dụ được đề cập trong bài học này.

🎉 CHÚC MỪNG! 🎉
