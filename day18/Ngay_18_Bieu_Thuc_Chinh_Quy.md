# 📘 Ngày 18 - Biểu Thức Chính Quy (Regular Expressions)

## Regular Expression là gì?

Regular Expression (RegEx) là chuỗi ký tự đặc biệt giúp tìm kiếm các mẫu (pattern) trong dữ liệu. RegEx có thể kiểm tra sự tồn tại của một mẫu trong các kiểu dữ liệu khác nhau. Để dùng RegEx trong Python, ta cần import module `re`.

```py
import re
```

## Các Phương Thức Trong Module re

| Phương thức | Mô tả |
|-------------|-------|
| `re.match()` | Tìm kiếm chỉ ở đầu chuỗi, trả về đối tượng match hoặc None |
| `re.search()` | Tìm kiếm ở bất kỳ vị trí nào trong chuỗi |
| `re.findall()` | Trả về danh sách tất cả các kết quả khớp |
| `re.split()` | Tách chuỗi tại các vị trí khớp, trả về danh sách |
| `re.sub()` | Thay thế một hoặc nhiều kết quả khớp trong chuỗi |

### match()

```py
# Cú pháp
re.match(substring, string, re.I)
# substring: mẫu cần tìm, string: văn bản, re.I: bỏ qua hoa/thường
```

```py
import re

txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

span = match.span()
print(span)         # (0, 15)

start, end = span
print(start, end)   # 0 15

substring = txt[start:end]
print(substring)    # I love to teach
```

> **Lưu ý:** `match()` chỉ khớp nếu văn bản **bắt đầu** bằng mẫu. Nếu không, trả về `None`.

### search()

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match = re.search('first', txt, re.I)
print(match)    # <re.Match object; span=(100, 105), match='first'>

span = match.span()
start, end = span
print(txt[start:end])  # first
```

`search()` tìm kiếm toàn bộ văn bản và trả về kết quả khớp **đầu tiên** tìm được.

### findall()

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

# Tìm cả Python và python
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

# Không dùng re.I
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']
```

### Thay Thế Chuỗi Con Với sub()

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('[Pp]ython', 'JavaScript', txt)
print(match_replaced)
# JavaScript is the most beautiful language...I recommend JavaScript for a first programming language
```

```py
# Xóa ký tự % trong văn bản
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.'''
matches = re.sub('%', '', txt)
print(matches)
# I am teacher and I love teaching.
```

## Tách Chuỗi Với re.split()

```py
txt = '''I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n', txt))
# ['I am teacher and I love teaching.',
#  'There is nothing as rewarding as educating and empowering people.',
#  'I found teaching more interesting than any other jobs.',
#  'Does this motivate you to be a teacher?']
```

## Viết Các Mẫu RegEx

### Tổng Hợp Ký Tự Đặc Biệt

| Ký tự | Ý nghĩa |
|-------|---------|
| `[]` | Tập hợp ký tự. Ví dụ: `[a-z]` là bất kỳ chữ cái thường nào |
| `\d` | Chữ số (0-9) |
| `\D` | Không phải chữ số |
| `.` | Bất kỳ ký tự nào ngoại trừ ký tự xuống dòng `\n` |
| `^` | Bắt đầu bằng. Trong `[]` có nghĩa là phủ định |
| `$` | Kết thúc bằng |
| `*` | Xuất hiện 0 hoặc nhiều lần |
| `+` | Xuất hiện 1 hoặc nhiều lần |
| `?` | Xuất hiện 0 hoặc 1 lần |
| `{3}` | Đúng 3 lần |
| `{3,}` | Ít nhất 3 lần |
| `{3,8}` | Từ 3 đến 8 lần |
| `\|` | Hoặc. Ví dụ: `apple\|banana` |
| `()` | Nhóm và bắt (capture and group) |

### Ví Dụ Dấu Ngoặc Vuông []

```py
regex_pattern = r'[Aa]pple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day keeps the doctor away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# Tìm cả Apple và Banana
regex_pattern = r'[Aa]pple|[Bb]anana'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

### Ký Tự Escape (\)

```py
regex_pattern = r'\d'
txt = 'This example was made on December 6, 2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']
```

### Một Hoặc Nhiều Lần (+)

```py
regex_pattern = r'\d+'
txt = 'This example was made on December 6, 2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### Dấu Chấm (.)

```py
regex_pattern = r'[a].'
txt = 'Apple and banana are fruits'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### Không hoặc Nhiều Lần (*)

```py
regex_pattern = r'[a].*'
txt = 'Apple and banana are fruits'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### Không hoặc Một Lần (?)

```py
txt = 'I am not sure if there is a convention how to write the word e-mail. Some people write it as email others may write it as Email or E-mail.'
regex_pattern = r'[Ee]-?mail'  # dấu '-' là tùy chọn
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

### Bộ Đếm (Quantifier) {}

```py
txt = 'This example was made on December 6, 2019 and revised on July 8, 2021'

regex_pattern = r'\d{4}'  # đúng 4 chữ số
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

regex_pattern = r'\d{1,4}'  # từ 1 đến 4 chữ số
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### Ký Tự ^ (Bắt Đầu / Phủ Định)

```py
txt = 'This regular expression example was made on December 6, 2019 and revised on July 8, 2021'

# Bắt đầu bằng
regex_pattern = r'^This'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

# Phủ định trong []
regex_pattern = r'[^A-Za-z ]+'  # không phải chữ cái và không phải dấu cách
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```

## 💻 Bài Tập: Ngày 18

### Bài tập cấp độ 1

1. Từ nào xuất hiện nhiều nhất trong đoạn văn sau?

```py
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
```

Kết quả mong đợi:
```sh
[(6, 'love'), (5, 'you'), (3, 'can'), (2, 'what'), (2, 'teaching'), ...]
```

2. Vị trí các hạt trên trục x: -12, -4, -3, -1 (âm), 0 (gốc tọa độ), 4 và 8 (dương). Trích xuất các số này từ văn bản và tìm khoảng cách giữa 2 hạt xa nhau nhất.

```py
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
distance = 8 - (-12)  # 20
```

### Bài tập cấp độ 2

1. Viết pattern kiểm tra xem chuỗi có phải là tên biến Python hợp lệ không:

```sh
is_valid_variable('first_name')  # True
is_valid_variable('first-name')  # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname')   # True
```

### Bài tập cấp độ 3

1. Làm sạch văn bản sau, rồi đếm 3 từ xuất hiện nhiều nhất:

```py
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Sau khi làm sạch:
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher

# print(most_frequent_words(cleaned_text))
# [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
```

🎉 CHÚC MỪNG! 🎉
