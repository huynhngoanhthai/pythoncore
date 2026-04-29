# 📘 Ngày 16 - Ngày Giờ Trong Python (Python Datetime)

## Module datetime

Python có module `datetime` để xử lý ngày và giờ.

```py
import datetime
print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', 'date', 'datetime', 'time', 'timedelta', 'timezone', 'tzinfo', ...]
```

Các thành phần chính ta sẽ dùng: `date`, `datetime`, `time`, `timedelta`.

## Lấy Thông Tin Ngày Giờ Hiện Tại

```py
from datetime import datetime

now = datetime.now()
print(now)                        # 2021-07-08 07:34:46.549883

day = now.day                     # ngày
month = now.month                 # tháng
year = now.year                   # năm
hour = now.hour                   # giờ
minute = now.minute               # phút
second = now.second               # giây
timestamp = now.timestamp()       # Unix timestamp

print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38
```

> **Lưu ý:** Timestamp (Unix timestamp) là số giây tính từ ngày 1 tháng 1 năm 1970 UTC.

## Định Dạng Ngày Giờ Với strftime

Dùng phương thức `strftime` để định dạng ngày giờ thành chuỗi:

```py
from datetime import datetime

now = datetime.now()

t = now.strftime("%H:%M:%S")
print("Giờ:", t)                   # Giờ: 18:21:40

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Định dạng 1:", time_one)    # Định dạng 1: 06/28/2022, 18:21:40

time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("Định dạng 2:", time_two)    # Định dạng 2: 28/06/2022, 18:21:40
```

Các ký hiệu strftime thường dùng:

| Ký hiệu | Ý nghĩa | Ví dụ |
|---------|---------|-------|
| `%Y` | Năm 4 chữ số | 2021 |
| `%m` | Tháng (01-12) | 07 |
| `%d` | Ngày (01-31) | 08 |
| `%H` | Giờ (00-23) | 07 |
| `%M` | Phút (00-59) | 38 |
| `%S` | Giây (00-59) | 46 |
| `%B` | Tên tháng đầy đủ | July |

## Chuyển Chuỗi Thành Ngày Giờ Với strptime

```py
from datetime import datetime

date_string = "5 December, 2019"
print("Chuỗi ngày:", date_string)       # Chuỗi ngày: 5 December, 2019

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Đối tượng ngày:", date_object)   # Đối tượng ngày: 2019-12-05 00:00:00
```

## Dùng date Từ Module datetime

```py
from datetime import date

d = date(2020, 1, 1)
print(d)                              # 2020-01-01
print('Ngày hiện tại:', d.today())    # 2019-12-05

today = date.today()
print("Năm hiện tại:", today.year)    # 2019
print("Tháng hiện tại:", today.month) # 12
print("Ngày hiện tại:", today.day)    # 5
```

## Đối Tượng time Để Biểu Diễn Giờ

```py
from datetime import time

# time(hour=0, minute=0, second=0)
a = time()
print("a =", a)          # a = 00:00:00

b = time(10, 30, 50)
print("b =", b)          # b = 10:30:50

c = time(hour=10, minute=30, second=50)
print("c =", c)          # c = 10:30:50

d = time(10, 30, 50, 200555)
print("d =", d)          # d = 10:30:50.200555
```

## Tính Khoảng Cách Giữa Hai Thời Điểm

```py
from datetime import date, datetime

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
print('Thời gian còn lại đến năm mới:', time_left_for_newyear)
# Thời gian còn lại đến năm mới: 27 days, 0:00:00

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print('Thời gian còn lại đến năm mới:', diff)
# Thời gian còn lại đến năm mới: 26 days, 23:01:00
```

## Dùng timedelta

```py
from datetime import timedelta

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
# t3 = 86 days, 22:56:50
```

## 💻 Bài Tập: Ngày 16

1. Lấy ngày, tháng, năm, giờ, phút và timestamp hiện tại từ module datetime.
2. Định dạng ngày hiện tại theo format: `"%m/%d/%Y, %H:%M:%S"`.
3. Ngày hôm nay là 5 tháng 12 năm 2019. Chuyển chuỗi ngày này thành đối tượng datetime.
4. Tính khoảng thời gian từ hiện tại đến năm mới.
5. Tính khoảng thời gian từ ngày 1 tháng 1 năm 1970 đến hiện tại.
6. Hãy nghĩ về những ứng dụng thực tế của module datetime. Ví dụ:
   - Phân tích chuỗi thời gian (time series)
   - Ghi lại timestamp các hoạt động trong ứng dụng
   - Đăng bài viết trên blog

🎉 CHÚC MỪNG! 🎉
