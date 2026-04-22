# 📘 Ngày 9 – Câu Lệnh Điều Kiện (Conditionals)

**Tác giả:** Asabeneh Yetayeh  
**Phiên bản thứ hai:** Tháng 7, 2021

---

- [📘 Ngày 9](#-ngày-9)
  - [Câu Lệnh Điều Kiện](#câu-lệnh-điều-kiện)
    - [Câu Lệnh If](#câu-lệnh-if)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [Dạng Rút Gọn](#dạng-rút-gọn)
    - [Điều Kiện Lồng Nhau](#điều-kiện-lồng-nhau)
    - [If Kết Hợp Toán Tử AND](#if-kết-hợp-toán-tử-and)
    - [If Kết Hợp Toán Tử OR](#if-kết-hợp-toán-tử-or)
  - [💻 Bài Tập: Ngày 9](#-bài-tập-ngày-9)
    - [Bài Tập: Mức 1](#bài-tập-mức-1)
    - [Bài Tập: Mức 2](#bài-tập-mức-2)
    - [Bài Tập: Mức 3](#bài-tập-mức-3)

---

# 📘 Ngày 9

## Câu Lệnh Điều Kiện

Theo mặc định, các câu lệnh trong Python được thực thi tuần tự từ trên xuống dưới. Nếu logic xử lý yêu cầu, luồng thực thi tuần tự có thể được thay đổi theo hai cách:

- **Thực thi có điều kiện:** một khối lệnh sẽ được thực thi nếu một biểu thức nhất định là đúng.
- **Thực thi lặp lại:** một khối lệnh sẽ được thực thi nhiều lần miễn là một biểu thức nhất định còn đúng.

Trong phần này, chúng ta sẽ tìm hiểu các câu lệnh `if`, `else`, `elif`. Các toán tử so sánh và logic đã học ở phần trước sẽ rất hữu ích ở đây.

### Câu Lệnh If

Trong Python và các ngôn ngữ lập trình khác, từ khóa `if` được dùng để kiểm tra điều kiện và thực thi khối lệnh nếu điều kiện đúng. Lưu ý thụt lề sau dấu hai chấm.

```py
# cú pháp
if dieu_kien:
    # khối lệnh này chạy khi điều kiện đúng
```

**Ví dụ 1:**

```py
a = 3
if a > 0:
    print('A là số dương')
# A là số dương
```

Như trong ví dụ trên, 3 lớn hơn 0 nên điều kiện đúng và khối lệnh được thực thi. Tuy nhiên, nếu điều kiện sai, ta sẽ không thấy kết quả gì. Để xử lý trường hợp điều kiện sai, ta cần thêm khối `else`.

### If Else

Nếu điều kiện đúng, khối `if` được thực thi; nếu sai, khối `else` được thực thi.

```py
# cú pháp
if dieu_kien:
    # khối lệnh khi điều kiện đúng
else:
    # khối lệnh khi điều kiện sai
```

**Ví dụ:**

```py
a = 3
if a < 0:
    print('A là số âm')
else:
    print('A là số dương')
```

Điều kiện trên sai, do đó khối `else` được thực thi. Nếu có nhiều hơn hai trường hợp thì sao? Ta có thể dùng `elif`.

### If Elif Else

Trong cuộc sống hàng ngày, chúng ta không chỉ đưa ra quyết định dựa trên một hay hai điều kiện mà là nhiều điều kiện. Tương tự, lập trình cũng đầy những điều kiện như vậy. Ta dùng `elif` khi có nhiều điều kiện cần kiểm tra.

```py
# cú pháp
if dieu_kien:
    # khối lệnh
elif dieu_kien:
    # khối lệnh
else:
    # khối lệnh
```

**Ví dụ:**

```py
a = 0
if a > 0:
    print('A là số dương')
elif a < 0:
    print('A là số âm')
else:
    print('A bằng 0')
```

### Dạng Rút Gọn

```py
# cú pháp
ket_qua = gia_tri_dung if dieu_kien else gia_tri_sai
```

**Ví dụ:**

```py
a = 3
print('A dương') if a > 0 else print('A âm')
# Điều kiện đầu tiên đúng, 'A dương' sẽ được in ra
```

### Điều Kiện Lồng Nhau

Các câu lệnh điều kiện có thể lồng vào nhau.

```py
# cú pháp
if dieu_kien:
    # khối lệnh
    if dieu_kien:
        # khối lệnh
```

**Ví dụ:**

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A là số dương và chẵn')
    else:
        print('A là số dương')
elif a == 0:
    print('A bằng 0')
else:
    print('A là số âm')
```

Ta có thể tránh viết điều kiện lồng nhau bằng cách dùng toán tử logic `and`.

### If Kết Hợp Toán Tử AND

```py
# cú pháp
if dieu_kien and dieu_kien:
    # khối lệnh
```

**Ví dụ:**

```py
a = 0
if a > 0 and a % 2 == 0:
    print('A là số nguyên dương và chẵn')
elif a > 0 and a % 2 != 0:
    print('A là số nguyên dương')
elif a == 0:
    print('A bằng 0')
else:
    print('A là số âm')
```

### If Kết Hợp Toán Tử OR

```py
# cú pháp
if dieu_kien or dieu_kien:
    # khối lệnh
```

**Ví dụ:**

```py
nguoi_dung = 'James'
cap_do_truy_cap = 3
if nguoi_dung == 'admin' or cap_do_truy_cap >= 4:
    print('Truy cập được cấp!')
else:
    print('Truy cập bị từ chối!')
```

🌕 Bạn đang làm rất tốt. Đừng bao giờ bỏ cuộc vì những điều vĩ đại cần có thời gian. Bạn vừa hoàn thành thử thách ngày 9 và đã tiến thêm 9 bước trên con đường đến sự vĩ đại. Hãy làm một số bài tập để rèn luyện não bộ và cơ bắp nhé.

## 💻 Bài Tập: Ngày 9

### Bài Tập: Mức 1

1. Nhập tuổi của người dùng bằng `input("Nhập tuổi của bạn: ")`. Nếu từ 18 tuổi trở lên, in ra: `Bạn đủ tuổi để lái xe.` Nếu dưới 18 tuổi, in ra số năm còn thiếu. Kết quả:

    ```sh
    Nhập tuổi của bạn: 30
    Bạn đủ tuổi để lái xe.

    Nhập tuổi của bạn: 15
    Bạn cần thêm 3 năm nữa để lái xe.
    ```

2. So sánh giá trị `tuoi_toi` và `tuoi_ban` bằng `if...else`. Ai lớn tuổi hơn (tôi hay bạn)? Dùng `input("Nhập tuổi của bạn: ")` để lấy đầu vào. Có thể dùng điều kiện lồng nhau để in `'năm'` cho chênh lệch 1 tuổi, `'tuổi'` cho chênh lệch lớn hơn. Kết quả:

    ```sh
    Nhập tuổi của bạn: 30
    Bạn lớn hơn tôi 5 tuổi.
    ```

3. Nhập hai số từ người dùng. Nếu `a` lớn hơn `b`, in `a lớn hơn b`; nếu `a` nhỏ hơn `b`, in `a nhỏ hơn b`; còn lại in `a bằng b`. Kết quả:

    ```sh
    Nhập số thứ nhất: 4
    Nhập số thứ hai: 3
    4 lớn hơn 3
    ```

### Bài Tập: Mức 2

1. Viết chương trình xếp loại học sinh theo điểm số:

    ```sh
    90-100 → A
    80-89  → B
    70-79  → C
    60-69  → D
    0-59   → F
    ```

2. Nhập tên tháng từ người dùng rồi xác định mùa:
    - Tháng 9, 10, 11 → Mùa Thu
    - Tháng 12, 1, 2 → Mùa Đông
    - Tháng 3, 4, 5 → Mùa Xuân
    - Tháng 6, 7, 8 → Mùa Hè

3. Cho danh sách trái cây sau:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    Nếu một loại trái cây chưa có trong danh sách, thêm vào và in danh sách đã cập nhật. Nếu đã có, in ra `'Loại trái cây đó đã có trong danh sách'`.

### Bài Tập: Mức 3

1. Cho từ điển `person` sau (bạn có thể tùy chỉnh!):

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
```

- Kiểm tra từ điển `person` có khóa `skills` không; nếu có, in ra kỹ năng ở giữa danh sách.
- Kiểm tra từ điển `person` có khóa `skills` không; nếu có, kiểm tra xem người đó có kỹ năng `'Python'` không và in ra kết quả.
- Nếu kỹ năng chỉ có JavaScript và React → in `'Đây là lập trình viên front-end'`; nếu có Node, Python, MongoDB → in `'Đây là lập trình viên back-end'`; nếu có React, Node và MongoDB → in `'Đây là lập trình viên full-stack'`; còn lại in `'Chức danh không xác định'`.
- Nếu người đó đã kết hôn và sống ở Phần Lan, in ra theo định dạng:

```py
Asabeneh Yetayeh sống ở Phần Lan. Anh ấy đã kết hôn.
```

🎉 CHÚC MỪNG! 🎉
