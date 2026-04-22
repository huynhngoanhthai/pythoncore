# 📘 Ngày 8 – Từ Điển (Dictionaries)

**Tác giả:** Asabeneh Yetayeh  
**Phiên bản thứ hai:** Tháng 7, 2021

---

- [📘 Ngày 8](#-ngày-8)
  - [Từ Điển](#từ-điển)
    - [Tạo Từ Điển](#tạo-từ-điển)
    - [Độ Dài Từ Điển](#độ-dài-từ-điển)
    - [Truy Cập Phần Tử Trong Từ Điển](#truy-cập-phần-tử-trong-từ-điển)
    - [Thêm Phần Tử Vào Từ Điển](#thêm-phần-tử-vào-từ-điển)
    - [Sửa Đổi Phần Tử Trong Từ Điển](#sửa-đổi-phần-tử-trong-từ-điển)
    - [Kiểm Tra Khóa Trong Từ Điển](#kiểm-tra-khóa-trong-từ-điển)
    - [Xóa Cặp Khóa-Giá Trị Khỏi Từ Điển](#xóa-cặp-khóa-giá-trị-khỏi-từ-điển)
    - [Chuyển Từ Điển Thành Danh Sách](#chuyển-từ-điển-thành-danh-sách)
    - [Xóa Toàn Bộ Nội Dung Từ Điển](#xóa-toàn-bộ-nội-dung-từ-điển)
    - [Xóa Hoàn Toàn Từ Điển](#xóa-hoàn-toàn-từ-điển)
    - [Sao Chép Từ Điển](#sao-chép-từ-điển)
    - [Lấy Danh Sách Khóa](#lấy-danh-sách-khóa)
    - [Lấy Danh Sách Giá Trị](#lấy-danh-sách-giá-trị)
  - [💻 Bài Tập: Ngày 8](#-bài-tập-ngày-8)

---

# 📘 Ngày 8

## Từ Điển

Từ điển là một tập hợp dữ liệu không có thứ tự, có thể thay đổi (mutable), được lưu trữ dưới dạng các cặp (khóa: giá trị).

### Tạo Từ Điển

Để tạo từ điển, ta dùng dấu ngoặc nhọn `{}` hoặc hàm built-in `dict()`.

```py
# cú pháp
tu_dien_rong = {}
# Từ điển có dữ liệu
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

**Ví dụ:**

```py
nguoi = {
    'ten': 'Asabeneh',
    'ho': 'Yetayeh',
    'tuoi': 250,
    'quoc_gia': 'Phần Lan',
    'da_ket_hon': True,
    'ky_nang': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dia_chi': {
        'duong': 'Space street',
        'ma_buu_dien': '02210'
    }
}
```

Từ điển trên cho thấy giá trị có thể là bất kỳ kiểu dữ liệu nào: chuỗi, boolean, danh sách, tuple, set hoặc một từ điển khác.

### Độ Dài Từ Điển

Hàm `len()` trả về số cặp khóa-giá trị trong từ điển.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**Ví dụ:**

```py
nguoi = {
    'ten': 'Asabeneh',
    'ho': 'Yetayeh',
    'tuoi': 250,
    'quoc_gia': 'Phần Lan',
    'da_ket_hon': True,
    'ky_nang': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dia_chi': {
        'duong': 'Space street',
        'ma_buu_dien': '02210'
    }
}
print(len(nguoi)) # 7
```

### Truy Cập Phần Tử Trong Từ Điển

Ta truy cập phần tử trong từ điển bằng cách dùng tên khóa.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
```

**Ví dụ:**

```py
nguoi = {
    'ten': 'Asabeneh',
    'ho': 'Yetayeh',
    'tuoi': 250,
    'quoc_gia': 'Phần Lan',
    'da_ket_hon': True,
    'ky_nang': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dia_chi': {
        'duong': 'Space street',
        'ma_buu_dien': '02210'
    }
}
print(nguoi['ten'])               # Asabeneh
print(nguoi['quoc_gia'])          # Phần Lan
print(nguoi['ky_nang'])           # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(nguoi['ky_nang'][0])        # JavaScript
print(nguoi['dia_chi']['duong'])  # Space street
print(nguoi['thanh_pho'])         # Lỗi!
```

Truy cập bằng khóa không tồn tại sẽ gây ra lỗi. Để tránh lỗi, hãy kiểm tra sự tồn tại của khóa trước, hoặc dùng phương thức `get()`. Phương thức `get()` trả về `None` nếu khóa không tồn tại.

```py
print(nguoi.get('ten'))        # Asabeneh
print(nguoi.get('quoc_gia'))   # Phần Lan
print(nguoi.get('ky_nang'))    # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(nguoi.get('thanh_pho'))  # None
```

### Thêm Phần Tử Vào Từ Điển

Ta có thể thêm cặp khóa-giá trị mới vào từ điển.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
```

**Ví dụ:**

```py
nguoi['chuc_danh'] = 'Giảng Viên'
nguoi['ky_nang'].append('HTML')
print(nguoi)
```

### Sửa Đổi Phần Tử Trong Từ Điển

Ta có thể thay đổi giá trị của các phần tử trong từ điển.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'gia-tri-moi'
```

**Ví dụ:**

```py
nguoi['ten'] = 'Eyob'
nguoi['tuoi'] = 252
```

### Kiểm Tra Khóa Trong Từ Điển

Dùng toán tử `in` để kiểm tra sự tồn tại của một khóa trong từ điển.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Xóa Cặp Khóa-Giá Trị Khỏi Từ Điển

- `pop(key)`: Xóa phần tử theo khóa chỉ định
- `popitem()`: Xóa phần tử cuối cùng
- `del`: Xóa phần tử theo khóa

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1')    # xóa key1
dct.popitem()      # xóa phần tử cuối
del dct['key2']    # xóa key2
```

**Ví dụ:**

```py
nguoi.pop('ten')         # Xóa phần tử 'ten'
nguoi.popitem()          # Xóa phần tử 'dia_chi'
del nguoi['da_ket_hon']  # Xóa phần tử 'da_ket_hon'
```

### Chuyển Từ Điển Thành Danh Sách

Phương thức `items()` chuyển từ điển thành danh sách các tuple.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())
# dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### Xóa Toàn Bộ Nội Dung Từ Điển

Dùng phương thức `clear()` để xóa tất cả phần tử trong từ điển.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### Xóa Hoàn Toàn Từ Điển

Dùng `del` để xóa hoàn toàn từ điển.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### Sao Chép Từ Điển

Dùng phương thức `copy()` để sao chép từ điển. Sao chép giúp tránh việc thay đổi ảnh hưởng đến từ điển gốc.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
ban_sao = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### Lấy Danh Sách Khóa

Phương thức `keys()` trả về tất cả các khóa của từ điển dưới dạng danh sách.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
khoa = dct.keys()
print(khoa) # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### Lấy Danh Sách Giá Trị

Phương thức `values()` trả về tất cả các giá trị của từ điển dưới dạng danh sách.

```py
# cú pháp
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
gia_tri = dct.values()
print(gia_tri) # dict_values(['value1', 'value2', 'value3', 'value4'])
```

🌕 Bạn thật tuyệt vời. Bây giờ bạn đã được trang bị sức mạnh của từ điển. Bạn vừa hoàn thành thử thách ngày 8 và đã tiến thêm 8 bước trên con đường đến sự vĩ đại. Hãy làm một số bài tập để rèn luyện não bộ và cơ bắp nhé.

## 💻 Bài Tập: Ngày 8

1. Tạo một từ điển rỗng tên là `dog`.
2. Thêm các khóa `name`, `color`, `breed`, `legs`, `age` vào từ điển `dog`.
3. Tạo từ điển `student` với các khóa: `first_name`, `last_name`, `gender`, `age`, `marital_status`, `skills`, `country`, `city` và `address`.
4. Lấy độ dài của từ điển `student`.
5. Lấy giá trị của `skills` và kiểm tra kiểu dữ liệu – phải là `list`.
6. Sửa đổi giá trị của `skills` bằng cách thêm một hoặc hai kỹ năng.
7. Lấy tất cả các khóa của từ điển dưới dạng list.
8. Lấy tất cả các giá trị của từ điển dưới dạng list.
9. Chuyển từ điển thành danh sách các tuple bằng phương thức `items()`.
10. Xóa một phần tử trong từ điển.
11. Xóa hoàn toàn một từ điển.

🎉 CHÚC MỪNG! 🎉
