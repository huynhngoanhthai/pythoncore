# 📘 Ngày 12 - Modules (Mô-đun)

## Modules là gì?

Module là một file chứa tập hợp các đoạn code hoặc hàm có thể được nhúng vào ứng dụng. Một module có thể là file chứa một biến đơn, một hàm, hoặc cả một codebase lớn.

## Tạo một Module

Để tạo module, ta viết code trong một file Python và lưu với đuôi `.py`. Tạo file `mymodule.py` trong thư mục dự án:

```py
# file mymodule.py
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

Tạo file `main.py` trong thư mục dự án và nhập file `mymodule.py`.

## Nhập (Import) một Module

Dùng từ khóa `import` và tên file:

```py
# file main.py
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))  # Asabeneh Yetayeh
```

## Nhập Hàm từ một Module

Một file có thể chứa nhiều hàm, ta có thể nhập tất cả theo nhiều cách:

```py
# file main.py
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh', 'Yetayeh'))
print(sum_two_nums(1, 9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

## Nhập Hàm và Đặt Lại Tên (Alias)

Khi nhập, ta có thể đặt lại tên (alias) cho module hoặc hàm:

```py
# file main.py
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh', 'Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p['firstname'])
```

## Nhập các Module Có Sẵn (Built-in)

Một số module phổ biến: `math`, `datetime`, `os`, `sys`, `random`, `statistics`, `collections`, `json`, `re`.

### Module OS

Module `os` cho phép thực hiện các thao tác với hệ điều hành:

```py
import os
os.mkdir('ten_thu_muc')   # Tạo thư mục
os.chdir('duong_dan')     # Đổi thư mục hiện tại
os.getcwd()               # Lấy thư mục hiện tại
os.rmdir()                # Xóa thư mục
```

### Module Sys

Module `sys` cung cấp các hàm và biến để thao tác với môi trường runtime. `sys.argv` trả về danh sách tham số dòng lệnh, index 0 là tên script:

```py
import sys
print('Chào {}. Hãy tận hưởng thử thách {}!'.format(sys.argv[1], sys.argv[2]))
```

Chạy lệnh: `python script.py Asabeneh 30DaysOfPython`

Kết quả: `Chào Asabeneh. Hãy tận hưởng thử thách 30DaysOfPython!`

Một số lệnh sys hữu ích:

```py
sys.exit()      # Thoát chương trình
sys.maxsize     # Giá trị số nguyên lớn nhất
sys.path        # Đường dẫn môi trường
sys.version     # Phiên bản Python đang dùng
```

### Module Statistics

Module `statistics` cung cấp các hàm thống kê toán học:

```py
from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))    # ~22.9  (trung bình)
print(median(ages))  # 23     (trung vị)
print(mode(ages))    # 20     (yếu vị)
print(stdev(ages))   # ~2.3   (độ lệch chuẩn)
```

### Module Math

Module chứa nhiều phép toán và hằng số toán học:

```py
import math
print(math.pi)           # 3.141592653589793 - hằng số pi
print(math.sqrt(2))      # 1.4142135623730951 - căn bậc hai
print(math.pow(2, 3))    # 8.0 - lũy thừa
print(math.floor(9.81))  # 9 - làm tròn xuống
print(math.ceil(9.81))   # 10 - làm tròn lên
print(math.log10(100))   # 2 - logarithm cơ số 10
```

Nhập nhiều hàm cùng lúc:

```py
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)        # 3.141592653589793
print(sqrt(2))   # 1.4142135623730951
print(pow(2, 3)) # 8.0
```

Nhập tất cả hoặc đặt alias:

```py
from math import *       # nhập tất cả
from math import pi as PI
print(PI)  # 3.141592653589793
```

Dùng `help(math)` hoặc `dir(math)` để xem danh sách hàm có trong module.

### Module String

```py
import string
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)         # 0123456789
print(string.punctuation)    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Module Random

`random()` trả về số thực ngẫu nhiên từ 0 đến 0.9999. `randint(a, b)` trả về số nguyên ngẫu nhiên trong đoạn `[a, b]`:

```py
from random import random, randint
print(random())        # số thực ngẫu nhiên từ 0 đến 0.9999
print(randint(5, 20))  # số nguyên ngẫu nhiên từ 5 đến 20
```

## 💻 Bài Tập: Ngày 12

### Bài tập cấp độ 1

1. Viết hàm tạo mã người dùng ngẫu nhiên gồm 6 ký tự/chữ số.
   ```py
   print(random_user_id())  # '1ee33d'
   ```

2. Khai báo hàm `user_id_gen_by_user` nhận 2 đầu vào: số ký tự và số lượng ID cần tạo.
   ```py
   print(user_id_gen_by_user())  # nhập: 5 5
   # kcsy2
   # SMFYb
   # bWmeq
   # ZXOYh
   # 2Rgxf
   ```

3. Viết hàm `rgb_color_gen` tạo màu RGB ngẫu nhiên (3 giá trị từ 0 đến 255).
   ```py
   print(rgb_color_gen())  # rgb(125,244,255)
   ```

### Bài tập cấp độ 2

1. Viết hàm `list_of_hexa_colors` trả về danh sách màu thập lục phân.
2. Viết hàm `list_of_rgb_colors` trả về danh sách màu RGB.
3. Viết hàm `generate_colors` tạo ra số lượng màu hexa hoặc rgb tùy ý.
   ```py
   generate_colors('hexa', 3)  # ['#a3e12f', '#03ed55', '#eb3d2b']
   generate_colors('hexa', 1)  # ['#b334ef']
   generate_colors('rgb', 3)   # ['rgb(5, 55, 175)', 'rgb(50, 105, 100)', 'rgb(15, 26, 80)']
   generate_colors('rgb', 1)   # ['rgb(33, 79, 176)']
   ```

### Bài tập cấp độ 3

1. Viết hàm `shuffle_list` nhận một danh sách và trả về danh sách đã xáo trộn.
2. Viết hàm trả về mảng gồm 7 số ngẫu nhiên không trùng nhau trong khoảng 0-9.

🎉 CHÚC MỪNG! 🎉
