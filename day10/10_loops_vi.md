<div align="center">
  <h1> 30 Ngày Học Python: Ngày 10 - Vòng Lặp</h1>
</div>

[<< Ngày 9](../09_Day_Conditionals/09_conditionals.md) | [Ngày 11 >>](../11_Day_Functions/11_functions.md)

- [📘 Ngày 10](#-ngày-10)
  - [Vòng Lặp](#vòng-lặp)
    - [Vòng Lặp While](#vòng-lặp-while)
    - [Break và Continue - Phần 1](#break-và-continue---phần-1)
    - [Vòng Lặp For](#vòng-lặp-for)
    - [Break và Continue - Phần 2](#break-và-continue---phần-2)
    - [Hàm Range](#hàm-range)
    - [Vòng Lặp For Lồng Nhau](#vòng-lặp-for-lồng-nhau)
    - [For Else](#for-else)
    - [Pass](#pass)
  - [💻 Bài Tập: Ngày 10](#-bài-tập-ngày-10)
    - [Bài Tập: Cấp Độ 1](#bài-tập-cấp-độ-1)
    - [Bài Tập: Cấp Độ 2](#bài-tập-cấp-độ-2)
    - [Bài Tập: Cấp Độ 3](#bài-tập-cấp-độ-3)

# 📘 Ngày 10

## Vòng Lặp

Cuộc sống luôn có những thói quen lặp đi lặp lại. Trong lập trình, chúng ta cũng thực hiện rất nhiều tác vụ lặp lại. Để xử lý những tác vụ như vậy, các ngôn ngữ lập trình sử dụng vòng lặp. Python cung cấp hai loại vòng lặp sau:

1. Vòng lặp while
2. Vòng lặp for

### Vòng Lặp While

Chúng ta dùng từ khóa _while_ để tạo vòng lặp while. Vòng lặp này dùng để thực thi một khối lệnh lặp đi lặp lại cho đến khi điều kiện cho trước không còn đúng nữa. Khi điều kiện trở thành sai, các dòng lệnh sau vòng lặp sẽ tiếp tục được thực thi.

```py
  # cú pháp
while điều_kiện:
    code ở đây
```

**Ví dụ:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
# in ra từ 0 đến 4
```

Trong vòng lặp while trên, điều kiện trở thành sai khi count bằng 5, và vòng lặp dừng lại.
Nếu muốn chạy thêm một đoạn code sau khi điều kiện không còn đúng nữa, ta có thể dùng _else_.

```py
  # cú pháp
while điều_kiện:
    code ở đây
else:
    code ở đây
```

**Ví dụ:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

Điều kiện vòng lặp trở thành sai khi count bằng 5, vòng lặp dừng lại và khối lệnh else được thực thi. Kết quả là số 5 sẽ được in ra.

### Break và Continue - Phần 1

- Break: Dùng khi chúng ta muốn thoát khỏi hoặc dừng vòng lặp.

```py
# cú pháp
while điều_kiện:
    code ở đây
    if điều_kiện_khác:
        break
```

**Ví dụ:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

Vòng lặp while trên chỉ in ra 0, 1, 2 — khi đến số 3 thì dừng.

- Continue: Dùng lệnh continue để bỏ qua lần lặp hiện tại và tiếp tục với lần lặp tiếp theo.

```py
  # cú pháp
while điều_kiện:
    code ở đây
    if điều_kiện_khác:
        continue
```

**Ví dụ:**

```py
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
```

Vòng lặp while trên chỉ in ra 0, 1, 2 và 4 (bỏ qua số 3).

### Vòng Lặp For

Từ khóa _for_ được dùng để tạo vòng lặp for, tương tự các ngôn ngữ lập trình khác nhưng có một số khác biệt về cú pháp. Vòng lặp for được dùng để duyệt qua một chuỗi (có thể là danh sách, tuple, từ điển, tập hợp hoặc chuỗi ký tự).

- Dùng vòng lặp For với danh sách (list)

```py
# cú pháp
for phần_tử in danh_sách:
    code ở đây
```

**Ví dụ:**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number là tên tạm thời để chỉ phần tử trong danh sách, chỉ hợp lệ bên trong vòng lặp này
    print(number)       # các số sẽ được in ra từng dòng, từ 0 đến 5
```

- Dùng vòng lặp For với chuỗi ký tự (string)

```py
# cú pháp
for phần_tử in chuỗi:
    code ở đây
```

**Ví dụ:**

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

- Dùng vòng lặp For với tuple

```py
# cú pháp
for phần_tử in tuple:
    code ở đây
```

**Ví dụ:**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- Vòng lặp For với từ điển (dictionary)
  Khi duyệt qua một từ điển, bạn nhận được các khóa (key) của từ điển đó.

```py
  # cú pháp
for phần_tử in từ_điển:
    code ở đây
```

**Ví dụ:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # cách này in ra cả khóa lẫn giá trị
```

- Dùng vòng lặp For với tập hợp (set)

```py
# cú pháp
for phần_tử in tập_hợp:
    code ở đây
```

**Ví dụ:**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break và Continue - Phần 2

Nhắc nhanh:
_Break_: Dùng khi muốn dừng vòng lặp trước khi hoàn thành.

```py
# cú pháp
for phần_tử in chuỗi:
    code ở đây
    if điều_kiện:
        break
```

**Ví dụ:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

Trong ví dụ trên, vòng lặp dừng lại khi đến số 3.

Continue: Dùng khi muốn bỏ qua một số bước trong vòng lặp.

```py
  # cú pháp
for phần_tử in chuỗi:
    code ở đây
    if điều_kiện:
        continue
```

**Ví dụ:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Số tiếp theo sẽ là ', number + 1) if number != 5 else print("Kết thúc vòng lặp") # điều kiện rút gọn cần cả if lẫn else
print('Ngoài vòng lặp')
```

Trong ví dụ trên, nếu số bằng 3, bước _sau_ điều kiện (nhưng vẫn trong vòng lặp) sẽ bị bỏ qua và vòng lặp tiếp tục nếu còn các lần lặp khác.

### Hàm Range

Hàm _range()_ dùng để trả về một dãy số. _range(start, end, step)_ nhận ba tham số: điểm bắt đầu, điểm kết thúc và bước nhảy. Mặc định, nó bắt đầu từ 0 và bước nhảy là 1. Hàm range cần ít nhất 1 đối số (điểm kết thúc).

Tạo các dãy số dùng range:

```py
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 đối số chỉ định điểm đầu và điểm cuối của dãy, bước mặc định là 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# đếm ngược từ điểm đầu đến điểm cuối
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]
```

```py
# cú pháp
for phần_tử in range(start, end, step):
```

**Ví dụ:**

```py
for number in range(11):
    print(number)   # in ra từ 0 đến 10, không bao gồm 11
```

### Vòng Lặp For Lồng Nhau

Chúng ta có thể viết vòng lặp bên trong một vòng lặp khác.

```py
# cú pháp
for x in y:
    for t in x:
        print(t)
```

**Ví dụ:**

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For Else

Nếu muốn thực thi một thông báo khi vòng lặp kết thúc, chúng ta dùng else.

```py
# cú pháp
for phần_tử in range(start, end, step):
    làm gì đó
else:
    print('Vòng lặp đã kết thúc')
```

**Ví dụ:**

```py
for number in range(11):
    print(number)   # in ra từ 0 đến 10, không bao gồm 11
else:
    print('Vòng lặp dừng tại', number)
```

### Pass

Trong Python, khi một câu lệnh là bắt buộc (sau dấu hai chấm) nhưng chúng ta không muốn thực thi bất kỳ code nào ở đó, chúng ta có thể viết từ khóa _pass_ để tránh lỗi. Pass cũng có thể được dùng như một chỗ giữ vị trí (placeholder) cho các câu lệnh trong tương lai.

**Ví dụ:**

```py
for number in range(6):
    pass
```

🌕 Bạn đã đạt được một cột mốc lớn, không gì có thể cản bạn lại. Tiếp tục nào! Bạn vừa hoàn thành thử thách ngày 10 và đang tiến thêm 10 bước trên con đường đến thành công. Bây giờ hãy làm một số bài tập để rèn luyện trí não và đôi tay nhé.

## 💻 Bài Tập: Ngày 10

### Bài Tập: Cấp Độ 1

1. Duyệt từ 0 đến 10 dùng vòng lặp for, sau đó làm tương tự với vòng lặp while.
2. Duyệt từ 10 về 0 dùng vòng lặp for, sau đó làm tương tự với vòng lặp while.
3. Viết một vòng lặp gọi print() bảy lần để in ra hình tam giác sau:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. Dùng vòng lặp lồng nhau để tạo ra kết quả sau:

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```

5. In ra bảng cửu chương theo dạng:

   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```

6. Duyệt qua danh sách `['Python', 'Numpy','Pandas','Django', 'Flask']` bằng vòng lặp for và in ra từng phần tử.
7. Dùng vòng lặp for để duyệt từ 0 đến 100 và chỉ in các số chẵn.
8. Dùng vòng lặp for để duyệt từ 0 đến 100 và chỉ in các số lẻ.

### Bài Tập: Cấp Độ 2

1. Dùng vòng lặp for để duyệt từ 0 đến 100 và in ra tổng của tất cả các số.

```sh
Tổng của tất cả các số là 5050.
```

2. Dùng vòng lặp for để duyệt từ 0 đến 100 và in ra tổng của tất cả các số chẵn và tổng của tất cả các số lẻ.

   ```sh
   Tổng tất cả số chẵn là 2550. Và tổng tất cả số lẻ là 2500.
   ```

### Bài Tập: Cấp Độ 3

1. Vào thư mục data và dùng file [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py). Duyệt qua danh sách các quốc gia và trích xuất tất cả quốc gia có chứa từ _land_.
2. Cho danh sách trái cây `['banana', 'orange', 'mango', 'lemon']`, hãy đảo ngược thứ tự bằng vòng lặp.
3. Vào thư mục data và dùng file [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py).
   1. Tổng số ngôn ngữ trong dữ liệu là bao nhiêu?
   2. Tìm mười ngôn ngữ được nói nhiều nhất trên thế giới từ dữ liệu.
   3. Tìm 10 quốc gia đông dân nhất thế giới.

🎉 CHÚC MỪNG! 🎉

[<< Ngày 9](../09_Day_Conditionals/09_conditionals.md) | [Ngày 11 >>](../11_Day_Functions/11_functions.md)
