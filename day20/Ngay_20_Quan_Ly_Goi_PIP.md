# 📘 Ngày 20 - Quản Lý Gói Python (PIP)

## PIP là gì?

PIP (Preferred Installer Program) là công cụ dùng để cài đặt các gói (package) Python. Package là module Python có thể chứa một hoặc nhiều module hoặc package khác. Thay vì tự viết mọi thứ, ta có thể cài đặt package và nhập vào ứng dụng.

## Cài Đặt PIP

```sh
pip install pip
```

Kiểm tra phiên bản pip:

```sh
pip --version
# pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)
```

## Cài Đặt Package Bằng pip

### Cài NumPy

NumPy (Numeric Python) là package phổ biến nhất trong cộng đồng machine learning và khoa học dữ liệu:

```sh
pip install numpy
```

```py
>>> import numpy
>>> numpy.version.version
'1.20.1'
>>> lst = [1, 2, 3, 4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr + 2
array([3, 4, 5, 6, 7])
```

### Cài Pandas

Pandas là thư viện phân tích dữ liệu mã nguồn mở, cung cấp cấu trúc dữ liệu hiệu suất cao:

```sh
pip install pandas
```

```py
>>> import pandas
```

### Dùng Module webbrowser (Có Sẵn)

Module `webbrowser` đã được cài sẵn với Python 3, có thể dùng để mở website:

```py
import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

for url in url_lists:
    webbrowser.open_new_tab(url)
```

## Gỡ Cài Đặt Package

```sh
pip uninstall ten_package
```

## Xem Danh Sách Package Đã Cài

```sh
pip list
```

## Xem Thông Tin Chi Tiết Package

```sh
pip show ten_package
```

```sh
pip show pandas
# Name: pandas
# Version: 1.2.3
# Summary: Powerful data structures for data analysis...
# Home-page: http://pandas.pydata.org
# License: BSD
# Location: /usr/local/lib/python3.7/site-packages
# Requires: python-dateutil, pytz, numpy
```

Thêm `--verbose` để xem chi tiết hơn:

```sh
pip show --verbose pandas
```

## PIP Freeze

Xuất danh sách tất cả package đã cài kèm phiên bản — thường dùng cho file `requirements.txt` khi triển khai dự án:

```sh
pip freeze
# docutils==0.11
# Jinja2==2.7.2
# MarkupSafe==0.19
# Pygments==1.6
# Sphinx==1.2.2
```

## Đọc Dữ Liệu Từ URL

Để kết nối mạng và thực hiện các thao tác CRUD (tạo, đọc, cập nhật, xóa), ta dùng package `requests`:

```sh
pip install requests
```

Các phương thức quan trọng của `requests`:
- `get()` — mở kết nối và lấy dữ liệu từ URL, trả về response object
- `status_code` — kiểm tra trạng thái (200 = thành công)
- `headers` — xem thông tin header
- `text` — lấy nội dung dạng văn bản
- `json()` — lấy dữ liệu dạng JSON

```py
import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
print(response)              # <Response [200]>
print(response.status_code)  # 200
print(response.headers)      # thông tin header
print(response.text)         # nội dung văn bản
```

Đọc dữ liệu từ API (trả về JSON):

```py
import requests

url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
print(response.status_code)  # 200
countries = response.json()
print(countries[:1])         # xem quốc gia đầu tiên
```

## Tạo Package Riêng

Để tổ chức nhiều file, ta tạo package. Package thực chất là một thư mục chứa file `__init__.py` và các module.

### Cấu Trúc Package

```sh
mypackage/
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

```py
# mypackage/arithmetic.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(a, b): return (a - b)
def multiple(a, b): return a * b
def division(a, b): return a / b
def remainder(a, b): return a % b
def power(a, b):    return a ** b
```

```py
# mypackage/greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, chào mừng đến với 30DaysOfPython!'
```

```py
# Dùng package
from mypackage import arithmetics
print(arithmetics.add_numbers(1, 2, 3, 5))  # 11
print(arithmetics.subtract(5, 3))           # 2
print(arithmetics.power(5, 3))              # 125

from mypackage import greet
print(greet.greet_person('Asabeneh', 'Yetayeh'))
```

> **Lưu ý:** File `__init__.py` (có thể để trống) là bắt buộc để Python nhận diện thư mục là một package.

## Một Số Package Phổ Biến

| Lĩnh vực | Package | Mô tả |
|----------|---------|-------|
| Cơ sở dữ liệu | SQLAlchemy | Truy cập hướng đối tượng tới nhiều CSDL |
| Web | Django | Framework web cấp cao |
| Web | Flask | Micro-framework nhẹ, linh hoạt |
| HTML Parser | BeautifulSoup4 | Phân tích HTML/XML |
| Khoa học dữ liệu | NumPy | Tính toán số học, mảng N chiều |
| Khoa học dữ liệu | Pandas | Phân tích và xử lý dữ liệu |
| Khoa học dữ liệu | SciPy | Tính toán khoa học |
| Machine Learning | Scikit-Learn | Thư viện ML phổ biến |
| Machine Learning | TensorFlow | Thư viện ML của Google |
| Machine Learning | Keras | API neural network cấp cao |
| Mạng | requests | Gửi HTTP request |

## 💻 Bài Tập: Ngày 20

1. Đọc URL sau và tìm 10 từ xuất hiện nhiều nhất:
   ```py
   romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
   ```

2. Đọc API mèo `https://api.thecatapi.com/v1/breeds` và tìm:
   - Min, max, mean, median, độ lệch chuẩn của cân nặng mèo (đơn vị metric)
   - Min, max, mean, median, độ lệch chuẩn của tuổi thọ mèo (năm)
   - Bảng tần suất quốc gia và giống mèo

3. Đọc API quốc gia `https://restcountries.eu/rest/v2/all` và tìm:
   - 10 quốc gia lớn nhất (diện tích)
   - 10 ngôn ngữ được nói nhiều nhất
   - Tổng số ngôn ngữ trong API

4. Đọc nội dung UCI `https://archive.ics.uci.edu/ml/datasets.php` (gợi ý: dùng BeautifulSoup4)

🎉 CHÚC MỪNG! 🎉
