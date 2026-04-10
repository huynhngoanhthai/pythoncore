<div align="center">
  <h1>30 Ngày Học Python: Ngày 4 - Chuỗi (Strings)</h1>
</div>

[<< Ngày 3](../03_Day_Operators/03_operators.md) | [Ngày 5 >>](../05_Day_Lists/05_lists.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Ngày 4](#ngày-4)
  - [Chuỗi](#chuỗi)
    - [Tạo Chuỗi](#tạo-chuỗi)
    - [Nối Chuỗi](#nối-chuỗi)
    - [Ký Tự Thoát Trong Chuỗi](#ký-tự-thoát-trong-chuỗi)
    - [Định Dạng Chuỗi](#định-dạng-chuỗi)
      - [Định Dạng Kiểu Cũ (Toán Tử %)](#định-dạng-kiểu-cũ-toán-tử-)
      - [Định Dạng Kiểu Mới (str.format)](#định-dạng-kiểu-mới-strformat)
      - [Nội Suy Chuỗi / f-Strings (Python 3.6+)](#nội-suy-chuỗi--f-strings-python-36)
    - [Chuỗi Python Là Dãy Ký Tự](#chuỗi-python-là-dãy-ký-tự)
      - [Giải Nén Ký Tự](#giải-nén-ký-tự)
      - [Truy Cập Ký Tự Bằng Chỉ Số](#truy-cập-ký-tự-bằng-chỉ-số)
      - [Cắt Chuỗi (Slicing)](#cắt-chuỗi-slicing)
      - [Đảo Ngược Chuỗi](#đảo-ngược-chuỗi)
      - [Bỏ Qua Ký Tự Khi Cắt](#bỏ-qua-ký-tự-khi-cắt)
    - [Các Phương Thức Chuỗi](#các-phương-thức-chuỗi)
  - [💻 Bài Tập - Ngày 4](#-bài-tập---ngày-4)

# Ngày 4

## Chuỗi

Văn bản là kiểu dữ liệu chuỗi (string). Bất kỳ dữ liệu nào được viết dưới dạng văn bản đều là chuỗi. Bất kỳ dữ liệu nào nằm trong dấu nháy đơn, nháy kép hoặc ba nháy đều là chuỗi. Có nhiều phương thức chuỗi và hàm có sẵn để xử lý kiểu dữ liệu chuỗi. Dùng hàm `len()` để kiểm tra độ dài của chuỗi.

### Tạo Chuỗi

```py
ky_tu = 'P'                # Chuỗi có thể là một ký tự đơn hoặc một đoạn văn bản
print(ky_tu)               # P
print(len(ky_tu))          # 1
loi_chao = 'Xin chào, Thế giới!'  # Chuỗi dùng nháy đơn hoặc nháy kép
print(loi_chao)            # Xin chào, Thế giới!
print(len(loi_chao))       # 19
cau = "Tôi hy vọng bạn đang tận hưởng 30 ngày học Python"
print(cau)
```

Chuỗi nhiều dòng được tạo bằng ba dấu nháy đơn (''') hoặc ba dấu nháy kép ("""). Xem ví dụ dưới đây:

```py
chuoi_nhieu_dong = '''Tôi là giáo viên và thích dạy học.
Tôi không tìm thấy điều gì có ý nghĩa hơn là giúp mọi người phát triển.
Đó là lý do tôi tạo ra khóa học 30 ngày Python.'''
print(chuoi_nhieu_dong)

# Cách khác làm điều tương tự
chuoi_nhieu_dong = """Tôi là giáo viên và thích dạy học.
Tôi không tìm thấy điều gì có ý nghĩa hơn là giúp mọi người phát triển.
Đó là lý do tôi tạo ra khóa học 30 ngày Python."""
print(chuoi_nhieu_dong)
```

### Nối Chuỗi

Chúng ta có thể kết nối các chuỗi lại với nhau. Việc ghép hoặc kết nối chuỗi gọi là nối chuỗi (concatenation). Xem ví dụ dưới đây:

```py
ten = 'Nguyễn'
ho = 'Văn An'
khoang_trang = ' '
ho_ten = ten + khoang_trang + ho
print(ho_ten)  # Nguyễn Văn An
# Kiểm tra độ dài chuỗi bằng hàm có sẵn len()
print(len(ten))   # 6
print(len(ho))    # 6
print(len(ten) > len(ho))  # False
print(len(ho_ten))         # 13
```

### Ký Tự Thoát Trong Chuỗi

Trong Python và các ngôn ngữ lập trình khác, dấu `\` theo sau bởi một ký tự là ký tự thoát (escape sequence). Hãy xem các ký tự thoát phổ biến nhất:

- `\n`: xuống dòng mới
- `\t`: Tab (8 dấu cách)
- `\\`: Dấu gạch chéo ngược
- `\'`: Dấu nháy đơn (')
- `\"`: Dấu nháy kép (")

Bây giờ hãy xem cách sử dụng các ký tự thoát trên qua ví dụ:

```py
print('Tôi hy vọng mọi người đang tận hưởng khóa học Python.\nBạn có không?')  # xuống dòng
print('Ngày\tChủ đề\tBài tập')   # thêm khoảng tab
print('Ngày 1\t5\t5')
print('Ngày 2\t6\t20')
print('Ngày 3\t5\t23')
print('Ngày 4\t1\t35')
print('Đây là ký hiệu gạch chéo ngược (\\)')  # để viết dấu \
print('Trong mọi ngôn ngữ lập trình đều bắt đầu với \"Xin chào, Thế giới!\"')

# Kết quả
# Tôi hy vọng mọi người đang tận hưởng khóa học Python.
# Bạn có không?
# Ngày  Chủ đề  Bài tập
# Ngày 1    5       5
# Ngày 2    6       20
# ...
```

### Định Dạng Chuỗi

#### Định Dạng Kiểu Cũ (Toán Tử %)

Trong Python có nhiều cách định dạng chuỗi. Toán tử `%` được dùng để định dạng một tập biến kết hợp với chuỗi định dạng chứa các ký hiệu đặc biệt như `%s`, `%d`, `%f`.

- `%s` - Chuỗi (hoặc bất kỳ đối tượng nào có thể biểu diễn dạng chuỗi)
- `%d` - Số nguyên
- `%f` - Số thực
- `%.nf` - Số thực với n chữ số sau dấu thập phân

```py
# Chỉ chuỗi
ten = 'Nguyễn Văn An'
ngon_ngu = 'Python'
chuoi_dinh_dang = 'Tôi là %s. Tôi học %s' % (ten, ngon_ngu)
print(chuoi_dinh_dang)

# Chuỗi và số
ban_kinh = 10
pi = 3.14
dien_tich = pi * ban_kinh ** 2
chuoi_dinh_dang = 'Diện tích hình tròn bán kính %d là %.2f.' % (ban_kinh, dien_tich)
print(chuoi_dinh_dang)

thu_vien = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
chuoi_dinh_dang = 'Các thư viện Python:%s' % (thu_vien)
print(chuoi_dinh_dang)
```

#### Định Dạng Kiểu Mới (str.format)

Cách định dạng này được giới thiệu từ Python phiên bản 3.

```py
ten = 'Nguyễn Văn An'
ngon_ngu = 'Python'
chuoi_dinh_dang = 'Tôi là {}. Tôi học {}'.format(ten, ngon_ngu)
print(chuoi_dinh_dang)

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))  # giới hạn 2 chữ số thập phân
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Kết quả:
# 4 + 3 = 7
# 4 - 3 = 1
# 4 * 3 = 12
# 4 / 3 = 1.33
# 4 % 3 = 1
# 4 // 3 = 1
# 4 ** 3 = 64

ban_kinh = 10
pi = 3.14
dien_tich = pi * ban_kinh ** 2
chuoi_kq = 'Diện tích hình tròn bán kính {} là {:.2f}.'.format(ban_kinh, dien_tich)
print(chuoi_kq)
```

#### Nội Suy Chuỗi / f-Strings (Python 3.6+)

f-strings là cách định dạng chuỗi mới và tiện lợi nhất. Chuỗi bắt đầu bằng chữ `f` và chúng ta có thể nhúng dữ liệu trực tiếp vào vị trí tương ứng.

```py
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Ví dụ thực tế
ten = 'Nguyễn Văn An'
tuoi = 25
quoc_gia = 'Việt Nam'
print(f'Tôi là {ten}. Tôi {tuoi} tuổi. Tôi sống ở {quoc_gia}.')
```

### Chuỗi Python Là Dãy Ký Tự

Chuỗi Python là dãy ký tự và chia sẻ các phương thức truy cập cơ bản với các dãy có thứ tự khác của Python như list và tuple. Cách đơn giản nhất để lấy từng ký tự là giải nén chúng vào các biến tương ứng.

#### Giải Nén Ký Tự

```py
ngon_ngu = 'Python'
a, b, c, d, e, f = ngon_ngu  # giải nén dãy ký tự vào biến
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
```

#### Truy Cập Ký Tự Bằng Chỉ Số

Trong lập trình, đếm bắt đầu từ 0. Do đó ký tự đầu tiên của chuỗi có chỉ số 0 và ký tự cuối có chỉ số bằng độ dài chuỗi trừ 1.

![String index](../images/string_index.png)

```py
ngon_ngu = 'Python'
ky_tu_dau = ngon_ngu[0]
print(ky_tu_dau)   # P
ky_tu_hai = ngon_ngu[1]
print(ky_tu_hai)   # y
chi_so_cuoi = len(ngon_ngu) - 1
ky_tu_cuoi = ngon_ngu[chi_so_cuoi]
print(ky_tu_cuoi)  # n
```

Nếu muốn bắt đầu từ bên phải, dùng chỉ số âm. -1 là chỉ số của ký tự cuối cùng.

```py
ngon_ngu = 'Python'
ky_tu_cuoi = ngon_ngu[-1]
print(ky_tu_cuoi)    # n
ky_tu_truoc_cuoi = ngon_ngu[-2]
print(ky_tu_truoc_cuoi)  # o
```

#### Cắt Chuỗi (Slicing)

Trong Python chúng ta có thể cắt chuỗi thành các chuỗi con.

```py
ngon_ngu = 'Python'
ba_ky_tu_dau = ngon_ngu[0:3]  # bắt đầu từ chỉ số 0, đến chỉ số 3 nhưng không bao gồm 3
print(ba_ky_tu_dau)   # Pyt
ba_ky_tu_cuoi = ngon_ngu[3:6]
print(ba_ky_tu_cuoi)  # hon
# Cách khác
ba_ky_tu_cuoi = ngon_ngu[-3:]
print(ba_ky_tu_cuoi)  # hon
ba_ky_tu_cuoi = ngon_ngu[3:]
print(ba_ky_tu_cuoi)  # hon
```

#### Đảo Ngược Chuỗi

Chúng ta có thể dễ dàng đảo ngược chuỗi trong Python:

```py
loi_chao = 'Xin chào, Thế giới!'
print(loi_chao[::-1])  # !ớiig ếhT ,òahc niX
```

#### Bỏ Qua Ký Tự Khi Cắt

Có thể bỏ qua ký tự khi cắt bằng cách truyền đối số bước (step):

```py
ngon_ngu = 'Python'
pto = ngon_ngu[0:6:2]  # lấy mỗi ký tự thứ 2
print(pto)  # Pto
```

### Các Phương Thức Chuỗi

Có rất nhiều phương thức chuỗi cho phép chúng ta định dạng chuỗi. Xem một số phương thức trong ví dụ sau:

- **capitalize()**: Viết hoa ký tự đầu tiên của chuỗi

```py
chuoi = 'ba mươi ngày học python'
print(chuoi.capitalize())  # 'Ba mươi ngày học python'
```

- **count()**: Đếm số lần xuất hiện của chuỗi con, count(chuoi_con, bat_dau, ket_thuc)

```py
chuoi = 'thirty days of python'
print(chuoi.count('y'))        # 3
print(chuoi.count('y', 7, 14)) # 1
print(chuoi.count('th'))       # 2
```

- **endswith()**: Kiểm tra chuỗi có kết thúc bằng ký tự/chuỗi chỉ định không

```py
chuoi = 'thirty days of python'
print(chuoi.endswith('on'))    # True
print(chuoi.endswith('tion'))  # False
```

- **expandtabs()**: Thay thế ký tự tab bằng dấu cách, mặc định kích thước tab là 8

```py
chuoi = 'thirty\tdays\tof\tpython'
print(chuoi.expandtabs())    # 'thirty  days    of      python'
print(chuoi.expandtabs(10))  # 'thirty    days      of        python'
```

- **find()**: Trả về chỉ số của lần xuất hiện đầu tiên của chuỗi con, trả về -1 nếu không tìm thấy

```py
chuoi = 'thirty days of python'
print(chuoi.find('y'))   # 5
print(chuoi.find('th'))  # 0
```

- **rfind()**: Trả về chỉ số của lần xuất hiện cuối cùng của chuỗi con, trả về -1 nếu không tìm thấy

```py
chuoi = 'thirty days of python'
print(chuoi.rfind('y'))   # 16
print(chuoi.rfind('th'))  # 17
```

- **format()**: Định dạng chuỗi

```py
ten = 'Nguyễn Văn An'
tuoi = 25
nghe = 'lập trình viên'
quoc_gia = 'Việt Nam'
cau = 'Tôi là {}. Tôi là {}. Tôi {} tuổi. Tôi sống ở {}.'.format(ten, nghe, tuoi, quoc_gia)
print(cau)

ban_kinh = 10
pi = 3.14
dien_tich = pi * ban_kinh ** 2
ket_qua = 'Diện tích hình tròn bán kính {} là {}'.format(str(ban_kinh), str(dien_tich))
print(ket_qua)
```

- **index()**: Trả về chỉ số thấp nhất của chuỗi con, báo lỗi ValueError nếu không tìm thấy

```py
chuoi = 'thirty days of python'
chuoi_con = 'da'
print(chuoi.index(chuoi_con))     # 7
print(chuoi.index(chuoi_con, 9))  # lỗi
```

- **rindex()**: Trả về chỉ số cao nhất của chuỗi con

```py
chuoi = 'thirty days of python'
chuoi_con = 'da'
print(chuoi.rindex(chuoi_con))     # 7
print(chuoi.rindex('on', 8))       # 19
```

- **isalnum()**: Kiểm tra ký tự chữ và số

```py
chuoi = 'ThirtyDaysPython'
print(chuoi.isalnum())   # True
chuoi = '30DaysPython'
print(chuoi.isalnum())   # True
chuoi = 'thirty days of python'
print(chuoi.isalnum())   # False, dấu cách không phải chữ-số
```

- **isalpha()**: Kiểm tra tất cả ký tự có phải chữ cái (a-z và A-Z) không

```py
chuoi = 'thirty days of python'
print(chuoi.isalpha())   # False, có dấu cách
chuoi = 'ThirtyDaysPython'
print(chuoi.isalpha())   # True
so = '123'
print(so.isalpha())      # False
```

- **isdecimal()**: Kiểm tra tất cả ký tự có phải số thập phân (0-9) không

```py
chuoi = 'thirty days of python'
print(chuoi.isdecimal())   # False
chuoi = '123'
print(chuoi.isdecimal())   # True
chuoi = '12 3'
print(chuoi.isdecimal())   # False, dấu cách không được phép
```

- **isdigit()**: Kiểm tra tất cả ký tự có phải chữ số (0-9 và một số ký tự unicode) không

```py
chuoi = 'Thirty'
print(chuoi.isdigit())   # False
chuoi = '30'
print(chuoi.isdigit())   # True
```

- **isnumeric()**: Kiểm tra tất cả ký tự có liên quan đến số không (chấp nhận thêm ký hiệu như ½)

```py
so = '10'
print(so.isnumeric())   # True
so = '\u00BD'           # ½
print(so.isnumeric())   # True
so = '10.5'
print(so.isnumeric())   # False
```

- **isidentifier()**: Kiểm tra xem chuỗi có phải là tên biến hợp lệ không

```py
chuoi = '30DaysOfPython'
print(chuoi.isidentifier())        # False, bắt đầu bằng số
chuoi = 'thirty_days_of_python'
print(chuoi.isidentifier())        # True
```

- **islower()**: Kiểm tra tất cả ký tự chữ cái có phải chữ thường không

```py
chuoi = 'thirty days of python'
print(chuoi.islower())   # True
chuoi = 'Thirty days of python'
print(chuoi.islower())   # False
```

- **isupper()**: Kiểm tra tất cả ký tự chữ cái có phải chữ hoa không

```py
chuoi = 'thirty days of python'
print(chuoi.isupper())   # False
chuoi = 'THIRTY DAYS OF PYTHON'
print(chuoi.isupper())   # True
```

- **join()**: Trả về chuỗi được nối

```py
cong_nghe_web = ['HTML', 'CSS', 'JavaScript', 'React']
ket_qua = ' '.join(cong_nghe_web)
print(ket_qua)   # 'HTML CSS JavaScript React'

ket_qua = '# '.join(cong_nghe_web)
print(ket_qua)   # 'HTML# CSS# JavaScript# React'
```

- **strip()**: Xóa tất cả ký tự chỉ định ở đầu và cuối chuỗi

```py
chuoi = 'thirty days of pythoonnn'
print(chuoi.strip('noth'))   # 'irty days of py'
```

- **replace()**: Thay thế chuỗi con bằng chuỗi khác

```py
chuoi = 'thirty days of python'
print(chuoi.replace('python', 'coding'))   # 'thirty days of coding'
```

- **split()**: Tách chuỗi dựa trên dấu phân cách

```py
chuoi = 'thirty days of python'
print(chuoi.split())         # ['thirty', 'days', 'of', 'python']
chuoi = 'thirty, days, of, python'
print(chuoi.split(', '))     # ['thirty', 'days', 'of', 'python']
```

- **title()**: Viết hoa chữ đầu mỗi từ

```py
chuoi = 'thirty days of python'
print(chuoi.title())   # Thirty Days Of Python
```

- **swapcase()**: Đổi chữ hoa thành chữ thường và ngược lại

```py
chuoi = 'thirty days of python'
print(chuoi.swapcase())    # THIRTY DAYS OF PYTHON
chuoi = 'Thirty Days Of Python'
print(chuoi.swapcase())    # tHIRTY dAYS oF pYTHON
```

- **startswith()**: Kiểm tra chuỗi có bắt đầu bằng chuỗi chỉ định không

```py
chuoi = 'thirty days of python'
print(chuoi.startswith('thirty'))   # True
chuoi = '30 days of python'
print(chuoi.startswith('thirty'))   # False
```

🌕 Bạn là người phi thường và có tiềm năng đáng kinh ngạc. Bạn vừa hoàn thành thử thách ngày 4 và đang tiến thêm bốn bước trên con đường đến sự vĩ đại. Bây giờ hãy làm một số bài tập cho não và cơ bắp của bạn.

## 💻 Bài Tập - Ngày 4

1. Nối các chuỗi 'Thirty', 'Days', 'Of', 'Python' thành một chuỗi duy nhất 'Thirty Days Of Python'.
2. Nối các chuỗi 'Coding', 'For', 'All' thành một chuỗi duy nhất 'Coding For All'.
3. Khai báo biến tên cong_ty và gán giá trị ban đầu là "Coding For All".
4. In biến cong_ty bằng hàm _print()_.
5. In độ dài chuỗi cong_ty bằng phương thức _len()_ và hàm _print()_.
6. Đổi tất cả ký tự thành chữ hoa bằng phương thức _upper()_.
7. Đổi tất cả ký tự thành chữ thường bằng phương thức _lower()_.
8. Dùng các phương thức capitalize(), title(), swapcase() để định dạng chuỗi _Coding For All_.
9. Cắt lấy từ đầu tiên của chuỗi _Coding For All_.
10. Kiểm tra xem chuỗi _Coding For All_ có chứa từ Coding không bằng phương thức index, find hoặc phương thức khác.
11. Thay thế từ coding trong chuỗi 'Coding For All' bằng Python.
12. Đổi "Python for Everyone" thành "Python for All" bằng phương thức replace hoặc phương thức khác.
13. Tách chuỗi 'Coding For All' dùng dấu cách làm ký tự phân cách (split()).
14. Tách chuỗi "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" theo dấu phẩy.
15. Ký tự ở chỉ số 0 của chuỗi _Coding For All_ là gì?
16. Chỉ số cuối cùng của chuỗi _Coding For All_ là bao nhiêu?
17. Ký tự ở chỉ số 10 trong chuỗi "Coding For All" là gì?
18. Tạo từ viết tắt cho tên 'Python For Everyone'.
19. Tạo từ viết tắt cho tên 'Coding For All'.
20. Dùng index để xác định vị trí xuất hiện đầu tiên của C trong Coding For All.
21. Dùng index để xác định vị trí xuất hiện đầu tiên của F trong Coding For All.
22. Dùng rfind để xác định vị trí xuất hiện cuối cùng của l trong Coding For All People.
23. Dùng index hoặc find để tìm vị trí xuất hiện đầu tiên của từ 'because' trong câu: 'You cannot end a sentence with because because because is a conjunction'
24. Dùng rindex để tìm vị trí xuất hiện cuối cùng của từ because trong câu: 'You cannot end a sentence with because because because is a conjunction'
25. Cắt lấy cụm 'because because because' trong câu: 'You cannot end a sentence with because because because is a conjunction'
26. Tìm vị trí xuất hiện đầu tiên của từ 'because' trong câu: 'You cannot end a sentence with because because because is a conjunction'
27. Cắt lấy cụm 'because because because' trong câu: 'You cannot end a sentence with because because because is a conjunction'
28. Chuỗi 'Coding For All' có bắt đầu bằng chuỗi con _Coding_ không?
29. Chuỗi 'Coding For All' có kết thúc bằng chuỗi con _coding_ không?
30. Xóa khoảng trắng ở đầu và cuối của chuỗi: '   Coding For All      '.
31. Biến nào trong hai biến sau trả về True khi dùng phương thức isidentifier():
    - 30DaysOfPython
    - thirty_days_of_python
32. Danh sách sau chứa tên một số thư viện Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Nối danh sách bằng chuỗi hash có dấu cách.
33. Dùng ký tự thoát xuống dòng để phân tách các câu sau.
    ```py
    Tôi đang tận hưởng thử thách này.
    Tôi tự hỏi điều gì sẽ đến tiếp theo.
    ```
34. Dùng ký tự thoát tab để viết các dòng sau.
    ```py
    Tên        Tuổi    Quốc gia    Thành phố
    Nguyễn An  25      Việt Nam    Hà Nội
    ```
35. Dùng phương thức định dạng chuỗi để hiển thị:
    ```sh
    ban_kinh = 10
    dien_tich = 3.14 * ban_kinh ** 2
    Diện tích hình tròn bán kính 10 là 314.0 mét vuông.
    ```
36. Dùng phương thức định dạng chuỗi để tạo kết quả:
    ```sh
    8 + 6 = 14
    8 - 6 = 2
    8 * 6 = 48
    8 / 6 = 1.33
    8 % 6 = 2
    8 // 6 = 1
    8 ** 6 = 262144
    ```

🎉 CHÚC MỪNG! 🎉

[<< Ngày 3](../03_Day_Operators/03_operators.md) | [Ngày 5 >>](../05_Day_Lists/05_lists.md)
