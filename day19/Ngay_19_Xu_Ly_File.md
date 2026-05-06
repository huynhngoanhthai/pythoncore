# 📘 Ngày 19 - Xử Lý File (File Handling)

## Xử Lý File là gì?

Xử lý file là phần quan trọng của lập trình, cho phép tạo, đọc, cập nhật và xóa file. Trong Python, ta dùng hàm có sẵn `open()` để xử lý dữ liệu.

```py
# Cú pháp
open('ten_file', mode)  # mode: r, a, w, x, t, b
```

Các chế độ (mode):

| Mode | Ý nghĩa |
|------|---------|
| `r` | Read (Đọc) — mặc định, báo lỗi nếu file không tồn tại |
| `a` | Append (Thêm vào cuối) — tạo file mới nếu chưa có |
| `w` | Write (Ghi) — ghi đè nội dung cũ, tạo file mới nếu chưa có |
| `x` | Create (Tạo) — báo lỗi nếu file đã tồn tại |
| `t` | Text — chế độ văn bản (mặc định) |
| `b` | Binary — chế độ nhị phân (ví dụ: ảnh) |

## Mở File Để Đọc

Chế độ mặc định của `open` là đọc (`r`), không cần chỉ định. File đã mở có các phương thức: `read()`, `readline()`, `readlines()`.

```py
f = open('./files/reading_file_example.txt')
print(f)  # <_io.TextIOWrapper name='...' mode='r' encoding='UTF-8'>
```

### read() — Đọc toàn bộ nội dung

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))  # <class 'str'>
print(txt)
f.close()
# output:
# This is an example to show how to open a file and read.
# This is the second line of the text.
```

Đọc giới hạn số ký tự:

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(txt)   # This is an
f.close()
```

### readline() — Đọc một dòng

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(line)  # This is an example to show how to open a file and read.
f.close()
```

### readlines() — Đọc tất cả dòng thành danh sách

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))  # <class 'list'>
print(lines)
# ['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
f.close()
```

### Dùng with (Tự động đóng file)

Cách tốt nhất để mở file — tự đóng sau khi dùng xong, không cần gọi `close()`:

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))  # <class 'list'>
    print(lines)
# ['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

## Mở File Để Ghi và Cập Nhật

### Thêm nội dung vào cuối file (mode 'a')

```py
with open('./files/reading_file_example.txt', 'a') as f:
    f.write('Đây là nội dung được thêm vào cuối file')
```

### Ghi mới / Ghi đè (mode 'w')

```py
with open('./files/writing_file_example.txt', 'w') as f:
    f.write('Nội dung này sẽ được ghi vào file mới tạo')
```

## Xóa File

Dùng module `os` để xóa file:

```py
import os
os.remove('./files/example.txt')
```

Kiểm tra trước khi xóa để tránh lỗi:

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('File không tồn tại')
```

## Các Loại File

### File .txt

Đây là định dạng phổ biến nhất, đã được đề cập ở trên.

### File .json

JSON (JavaScript Object Notation) thực chất là chuỗi ký tự dạng dictionary của Python.

```py
# dictionary Python
person_dct = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}

# JSON là dạng chuỗi của dictionary
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''
```

#### Chuyển JSON thành Dictionary

Dùng `json.loads()`:

```py
import json

person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''

person_dct = json.loads(person_json)
print(type(person_dct))       # <class 'dict'>
print(person_dct['name'])     # Asabeneh
```

#### Chuyển Dictionary thành JSON

Dùng `json.dumps()`:

```py
import json

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}

person_json = json.dumps(person, indent=4)  # indent=4 để dễ đọc
print(type(person_json))  # <class 'str'>
print(person_json)
```

#### Lưu Dữ Liệu Thành File JSON

```py
import json

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}

with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

### File .csv

CSV (Comma Separated Values) là định dạng file đơn giản dùng để lưu dữ liệu dạng bảng, rất phổ biến trong khoa học dữ liệu.

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

```py
import csv

with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Tên cột: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} là giáo viên. Sống ở {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Số dòng: {line_count}')
```

### File .xlsx

Để đọc file Excel, cần cài package `xlrd`:

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names())
```

### File .xml

XML là định dạng dữ liệu có cấu trúc, trông giống HTML nhưng thẻ không được định nghĩa sẵn:

```xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScript</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

```py
import xml.etree.ElementTree as ET

tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Thẻ gốc:', root.tag)         # person
print('Thuộc tính:', root.attrib)   # {'gender': 'male'}
for child in root:
    print('Trường:', child.tag)
```

## 💻 Bài Tập: Ngày 19

### Bài tập cấp độ 1

1. Viết hàm đếm số dòng và số từ trong một file văn bản. Thực hiện với các file sau:
   - obama_speech.txt
   - michelle_obama_speech.txt
   - donald_speech.txt
   - melina_trump_speech.txt

2. Đọc file countries_data.json, tạo hàm tìm 10 ngôn ngữ được nói nhiều nhất:
   ```py
   print(most_spoken_languages(filename='./data/countries_data.json', 10))
   # [(91, 'English'), (45, 'French'), (25, 'Arabic'), ...]
   ```

3. Đọc file countries_data.json, tạo hàm tìm 10 quốc gia đông dân nhất:
   ```py
   print(most_populated_countries(filename='./data/countries_data.json', 10))
   # [{'country': 'China', 'population': 1377422166}, ...]
   ```

### Bài tập cấp độ 2

1. Trích xuất tất cả địa chỉ email từ file email_exchange_big.txt thành danh sách.
2. Viết hàm `find_most_common_words` nhận file/chuỗi và số nguyên dương, trả về danh sách tuple các từ xuất hiện nhiều nhất theo thứ tự giảm dần.
3. Dùng hàm trên tìm 10 từ xuất hiện nhiều nhất trong bài diễn văn của Obama, Michelle, Trump và Melina.
4. Viết ứng dụng kiểm tra độ tương đồng giữa hai đoạn văn bản.
5. Tìm 10 từ lặp lại nhiều nhất trong file romeo_and_juliet.txt.
6. Đọc file hacker_news.csv và tìm:
   - Số dòng chứa từ `python` hoặc `Python`
   - Số dòng chứa `JavaScript`, `javascript` hoặc `Javascript`
   - Số dòng chứa `Java` nhưng không chứa `JavaScript`

🎉 CHÚC MỪNG! 🎉
