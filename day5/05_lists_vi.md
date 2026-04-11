<div align="center">
  <h1>30 Ngày Học Python: Ngày 5 - Danh Sách (Lists)</h1>
</div>

[<< Ngày 4](../04_Day_Strings/04_strings.md) | [Ngày 6 >>](../06_Day_Tuples/06_tuples.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Ngày 5](#ngày-5)
  - [Danh Sách](#danh-sách)
    - [Tạo Danh Sách](#tạo-danh-sách)
    - [Truy Cập Phần Tử Bằng Chỉ Số Dương](#truy-cập-phần-tử-bằng-chỉ-số-dương)
    - [Truy Cập Phần Tử Bằng Chỉ Số Âm](#truy-cập-phần-tử-bằng-chỉ-số-âm)
    - [Giải Nén Danh Sách](#giải-nén-danh-sách)
    - [Cắt Danh Sách (Slicing)](#cắt-danh-sách-slicing)
    - [Chỉnh Sửa Danh Sách](#chỉnh-sửa-danh-sách)
    - [Kiểm Tra Phần Tử Trong Danh Sách](#kiểm-tra-phần-tử-trong-danh-sách)
    - [Thêm Phần Tử Vào Cuối Danh Sách](#thêm-phần-tử-vào-cuối-danh-sách)
    - [Chèn Phần Tử Vào Vị Trí Chỉ Định](#chèn-phần-tử-vào-vị-trí-chỉ-định)
    - [Xóa Phần Tử Bằng remove()](#xóa-phần-tử-bằng-remove)
    - [Xóa Phần Tử Bằng pop()](#xóa-phần-tử-bằng-pop)
    - [Xóa Phần Tử Bằng del](#xóa-phần-tử-bằng-del)
    - [Xóa Toàn Bộ Danh Sách](#xóa-toàn-bộ-danh-sách)
    - [Sao Chép Danh Sách](#sao-chép-danh-sách)
    - [Nối Danh Sách](#nối-danh-sách)
    - [Đếm Phần Tử](#đếm-phần-tử)
    - [Tìm Chỉ Số Của Phần Tử](#tìm-chỉ-số-của-phần-tử)
    - [Đảo Ngược Danh Sách](#đảo-ngược-danh-sách)
    - [Sắp Xếp Danh Sách](#sắp-xếp-danh-sách)
  - [💻 Bài Tập: Ngày 5](#-bài-tập-ngày-5)

# Ngày 5

## Danh Sách

Trong Python có bốn kiểu dữ liệu tập hợp:

- **List (Danh sách)**: Tập hợp có thứ tự và có thể thay đổi (mutable). Cho phép phần tử trùng lặp.
- **Tuple**: Tập hợp có thứ tự và không thể thay đổi (immutable). Cho phép phần tử trùng lặp.
- **Set (Tập hợp)**: Tập hợp không có thứ tự, không có chỉ số và không thể sửa, nhưng có thể thêm phần tử mới. Không cho phép trùng lặp.
- **Dictionary (Từ điển)**: Tập hợp không có thứ tự, có thể thay đổi và có chỉ số. Không có phần tử trùng lặp.

Danh sách là tập hợp các kiểu dữ liệu khác nhau, có thứ tự và có thể chỉnh sửa (mutable). Danh sách có thể rỗng hoặc chứa các phần tử thuộc nhiều kiểu dữ liệu khác nhau.

### Tạo Danh Sách

Trong Python có hai cách tạo danh sách:

- Dùng hàm có sẵn `list()`

```py
# cú pháp
ds = list()
```

```py
ds_rong = list()  # danh sách rỗng, không có phần tử nào
print(len(ds_rong))  # 0
```

- Dùng dấu ngoặc vuông `[]`

```py
# cú pháp
ds = []
```

```py
ds_rong = []  # danh sách rỗng
print(len(ds_rong))  # 0
```

Danh sách có giá trị ban đầu. Dùng `len()` để tìm độ dài danh sách:

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
rau_cu   = ['cà chua', 'khoai tây', 'bắp cải', 'hành', 'cà rốt']
san_pham_dong_vat = ['sữa', 'thịt', 'bơ', 'sữa chua']
cong_nghe_web = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
quoc_gia = ['Việt Nam', 'Nhật Bản', 'Hàn Quốc', 'Thái Lan', 'Singapore']

print('Trái cây:', trai_cay)
print('Số lượng trái cây:', len(trai_cay))
print('Rau củ:', rau_cu)
print('Số lượng rau củ:', len(rau_cu))
print('Sản phẩm động vật:', san_pham_dong_vat)
print('Công nghệ web:', cong_nghe_web)
print('Quốc gia:', quoc_gia)
```

```sh
# Kết quả
Trái cây: ['chuối', 'cam', 'xoài', 'chanh']
Số lượng trái cây: 4
Rau củ: ['cà chua', 'khoai tây', 'bắp cải', 'hành', 'cà rốt']
Số lượng rau củ: 5
Sản phẩm động vật: ['sữa', 'thịt', 'bơ', 'sữa chua']
Công nghệ web: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
Quốc gia: ['Việt Nam', 'Nhật Bản', 'Hàn Quốc', 'Thái Lan', 'Singapore']
```

Danh sách có thể chứa nhiều kiểu dữ liệu khác nhau:

```py
ds_hon_hop = ['Nguyễn Văn An', 25, True, {'quoc_gia': 'Việt Nam', 'thanh_pho': 'Hà Nội'}]
```

### Truy Cập Phần Tử Bằng Chỉ Số Dương

Chúng ta truy cập từng phần tử trong danh sách bằng chỉ số. Chỉ số danh sách bắt đầu từ 0.

![List index](../images/list_index.png)

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
trai_cay_dau = trai_cay[0]   # truy cập phần tử đầu tiên
print(trai_cay_dau)           # chuối
trai_cay_hai = trai_cay[1]
print(trai_cay_hai)           # cam
trai_cay_cuoi = trai_cay[3]
print(trai_cay_cuoi)          # chanh
# Chỉ số cuối
chi_so_cuoi = len(trai_cay) - 1
print(trai_cay[chi_so_cuoi])  # chanh
```

### Truy Cập Phần Tử Bằng Chỉ Số Âm

Chỉ số âm đếm từ cuối danh sách. -1 là phần tử cuối, -2 là phần tử áp cuối.

![List negative indexing](../images/list_negative_indexing.png)

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
trai_cay_dau    = trai_cay[-4]
trai_cay_cuoi   = trai_cay[-1]
trai_cay_ap_cuoi = trai_cay[-2]
print(trai_cay_dau)      # chuối
print(trai_cay_cuoi)     # chanh
print(trai_cay_ap_cuoi)  # xoài
```

### Giải Nén Danh Sách

```py
ds = ['pt1', 'pt2', 'pt3', 'pt4', 'pt5']
pt_1, pt_2, pt_3, *con_lai = ds
print(pt_1)      # pt1
print(pt_2)      # pt2
print(pt_3)      # pt3
print(con_lai)   # ['pt4', 'pt5']
```

```py
# Ví dụ 1
trai_cay = ['chuối', 'cam', 'xoài', 'chanh', 'chanh dây', 'táo']
qua_1, qua_2, qua_3, *con_lai = trai_cay
print(qua_1)      # chuối
print(qua_2)      # cam
print(qua_3)      # xoài
print(con_lai)    # ['chanh', 'chanh dây', 'táo']

# Ví dụ 2 — giải nén với phần tử đầu và cuối
dau, hai, ba, *giua, cuoi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(dau)    # 1
print(hai)    # 2
print(ba)     # 3
print(giua)   # [4, 5, 6, 7, 8, 9]
print(cuoi)   # 10

# Ví dụ 3
quoc_gia = ['Đức', 'Pháp', 'Bỉ', 'Thụy Điển', 'Đan Mạch', 'Phần Lan', 'Na Uy', 'Iceland', 'Estonia']
de, ph, bi, tv, *bac_au, es = quoc_gia
print(de)      # Đức
print(ph)      # Pháp
print(bi)      # Bỉ
print(tv)      # Thụy Điển
print(bac_au)  # ['Đan Mạch', 'Phần Lan', 'Na Uy', 'Iceland']
print(es)      # Estonia
```

### Cắt Danh Sách (Slicing)

- **Chỉ số dương**: Chỉ định phạm vi với start, stop và step — trả về danh sách mới.

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
tat_ca     = trai_cay[0:4]   # lấy tất cả
tat_ca     = trai_cay[0:]    # không ghi stop → lấy đến hết
cam_xoai   = trai_cay[1:3]   # không bao gồm chỉ số 3
tu_cam_den = trai_cay[1:]
cach_mot   = trai_cay[::2]   # bước 2: ['chuối', 'xoài']
```

- **Chỉ số âm**: Dùng chỉ số âm để cắt từ cuối.

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
tat_ca        = trai_cay[-4:]     # lấy tất cả
cam_xoai      = trai_cay[-3:-1]   # ['cam', 'xoài']
cam_den_cuoi  = trai_cay[-3:]     # ['cam', 'xoài', 'chanh']
dao_nguoc     = trai_cay[::-1]    # ['chanh', 'xoài', 'cam', 'chuối']
```

### Chỉnh Sửa Danh Sách

Danh sách có thể thay đổi — chúng ta có thể sửa giá trị phần tử bằng chỉ số:

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
trai_cay[0] = 'bơ'
print(trai_cay)        # ['bơ', 'cam', 'xoài', 'chanh']
trai_cay[1] = 'táo'
print(trai_cay)        # ['bơ', 'táo', 'xoài', 'chanh']
chi_so_cuoi = len(trai_cay) - 1
trai_cay[chi_so_cuoi] = 'chanh dây'
print(trai_cay)        # ['bơ', 'táo', 'xoài', 'chanh dây']
```

### Kiểm Tra Phần Tử Trong Danh Sách

Dùng toán tử `in` để kiểm tra một phần tử có trong danh sách không:

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
co_chuoi = 'chuối' in trai_cay
print(co_chuoi)   # True
co_chanh_day = 'chanh dây' in trai_cay
print(co_chanh_day)  # False
```

### Thêm Phần Tử Vào Cuối Danh Sách

Dùng phương thức `append()` để thêm phần tử vào cuối danh sách:

```py
# cú pháp
ds = list()
ds.append(phan_tu)
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
trai_cay.append('táo')
print(trai_cay)   # ['chuối', 'cam', 'xoài', 'chanh', 'táo']
trai_cay.append('chanh dây')
print(trai_cay)   # ['chuối', 'cam', 'xoài', 'chanh', 'táo', 'chanh dây']
```

### Chèn Phần Tử Vào Vị Trí Chỉ Định

Dùng `insert()` để chèn phần tử vào một vị trí chỉ định. Các phần tử sau sẽ dịch sang phải. `insert()` nhận hai tham số: chỉ số và phần tử cần chèn.

```py
# cú pháp
ds = ['pt1', 'pt2']
ds.insert(chi_so, phan_tu)
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
trai_cay.insert(2, 'táo')   # chèn táo giữa cam và xoài
print(trai_cay)   # ['chuối', 'cam', 'táo', 'xoài', 'chanh']
trai_cay.insert(3, 'chanh dây')
print(trai_cay)   # ['chuối', 'cam', 'táo', 'chanh dây', 'xoài', 'chanh']
```

### Xóa Phần Tử Bằng remove()

Phương thức `remove()` xóa phần tử được chỉ định (lần xuất hiện đầu tiên):

```py
# cú pháp
ds = ['pt1', 'pt2']
ds.remove(phan_tu)
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh', 'chuối']
trai_cay.remove('chuối')
print(trai_cay)   # ['cam', 'xoài', 'chanh', 'chuối'] — xóa lần đầu tiên
trai_cay.remove('chanh')
print(trai_cay)   # ['cam', 'xoài', 'chuối']
```

### Xóa Phần Tử Bằng pop()

Phương thức `pop()` xóa phần tử tại chỉ số chỉ định (hoặc phần tử cuối nếu không truyền chỉ số):

```py
# cú pháp
ds = ['pt1', 'pt2']
ds.pop()          # xóa phần tử cuối
ds.pop(chi_so)    # xóa phần tử tại chỉ số
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
trai_cay.pop()
print(trai_cay)   # ['chuối', 'cam', 'xoài']
trai_cay.pop(0)
print(trai_cay)   # ['cam', 'xoài']
```

### Xóa Phần Tử Bằng del

Từ khóa `del` xóa phần tử tại chỉ số chỉ định, có thể xóa một phạm vi hoặc xóa toàn bộ danh sách:

```py
# cú pháp
ds = ['pt1', 'pt2']
del ds[chi_so]   # xóa một phần tử
del ds           # xóa hoàn toàn danh sách
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh', 'kiwi', 'chanh dây']
del trai_cay[0]
print(trai_cay)        # ['cam', 'xoài', 'chanh', 'kiwi', 'chanh dây']
del trai_cay[1]
print(trai_cay)        # ['cam', 'chanh', 'kiwi', 'chanh dây']
del trai_cay[1:3]      # xóa phần tử chỉ số 1 và 2, không bao gồm 3
print(trai_cay)        # ['cam', 'chanh dây']
del trai_cay
print(trai_cay)        # NameError: name 'trai_cay' is not defined
```

### Xóa Toàn Bộ Danh Sách

Phương thức `clear()` làm rỗng danh sách (danh sách vẫn tồn tại nhưng không có phần tử):

```py
# cú pháp
ds = ['pt1', 'pt2']
ds.clear()
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
trai_cay.clear()
print(trai_cay)   # []
```

### Sao Chép Danh Sách

Gán `ds2 = ds1` chỉ tạo tham chiếu — thay đổi ds2 sẽ ảnh hưởng đến ds1. Dùng `copy()` để tạo bản sao độc lập:

```py
# cú pháp
ds = ['pt1', 'pt2']
ds_sao_chep = ds.copy()
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
trai_cay_copy = trai_cay.copy()
print(trai_cay_copy)   # ['chuối', 'cam', 'xoài', 'chanh']

# Minh họa sự khác biệt
ds1 = [1, 2, 3]
ds2 = ds1          # ds2 là tham chiếu của ds1
ds2[0] = 99
print(ds1)         # [99, 2, 3] — ds1 bị thay đổi theo!

ds3 = ds1.copy()   # ds3 là bản sao độc lập
ds3[0] = 0
print(ds1)         # [99, 2, 3] — ds1 không bị ảnh hưởng
```

### Nối Danh Sách

Có hai cách nối danh sách trong Python:

- **Toán tử cộng (+)**

```py
# cú pháp
ds3 = ds1 + ds2
```

```py
so_duong = [1, 2, 3, 4, 5]
so_khong = [0]
so_am    = [-5, -4, -3, -2, -1]
so_nguyen = so_am + so_khong + so_duong
print(so_nguyen)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
rau_cu   = ['cà chua', 'khoai tây', 'bắp cải', 'hành', 'cà rốt']
trai_cay_va_rau = trai_cay + rau_cu
print(trai_cay_va_rau)
```

- **Phương thức extend()**

```py
# cú pháp
ds1 = ['pt1', 'pt2']
ds2 = ['pt3', 'pt4', 'pt5']
ds1.extend(ds2)   # ds1 = ['pt1', 'pt2', 'pt3', 'pt4', 'pt5']
```

```py
so1 = [0, 1, 2, 3]
so2 = [4, 5, 6]
so1.extend(so2)
print('Các số:', so1)   # Các số: [0, 1, 2, 3, 4, 5, 6]

so_am    = [-5, -4, -3, -2, -1]
so_duong = [1, 2, 3, 4, 5]
so_khong = [0]
so_am.extend(so_khong)
so_am.extend(so_duong)
print('Số nguyên:', so_am)  # Số nguyên: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
```

### Đếm Phần Tử

Phương thức `count()` trả về số lần một phần tử xuất hiện trong danh sách:

```py
# cú pháp
ds = ['pt1', 'pt2']
ds.count(phan_tu)
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
print(trai_cay.count('cam'))   # 1
tuoi = [22, 19, 24, 25, 26, 24, 25, 24]
print(tuoi.count(24))          # 3
```

### Tìm Chỉ Số Của Phần Tử

Phương thức `index()` trả về chỉ số của phần tử trong danh sách:

```py
# cú pháp
ds = ['pt1', 'pt2']
ds.index(phan_tu)
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
print(trai_cay.index('cam'))   # 1
tuoi = [22, 19, 24, 25, 26, 24, 25, 24]
print(tuoi.index(24))          # 2 — lần xuất hiện đầu tiên
```

### Đảo Ngược Danh Sách

Phương thức `reverse()` đảo ngược thứ tự các phần tử trong danh sách:

```py
# cú pháp
ds = ['pt1', 'pt2']
ds.reverse()
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
trai_cay.reverse()
print(trai_cay)   # ['chanh', 'xoài', 'cam', 'chuối']

tuoi = [22, 19, 24, 25, 26, 24, 25, 24]
tuoi.reverse()
print(tuoi)       # [24, 25, 24, 26, 25, 24, 19, 22]
```

### Sắp Xếp Danh Sách

Dùng `sort()` hoặc hàm có sẵn `sorted()` để sắp xếp danh sách.

- **sort()**: Sắp xếp tăng dần và thay đổi danh sách gốc

```py
# cú pháp
ds = ['pt1', 'pt2']
ds.sort()                 # tăng dần
ds.sort(reverse=True)     # giảm dần
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
trai_cay.sort()
print(trai_cay)              # sắp xếp theo thứ tự bảng chữ cái
trai_cay.sort(reverse=True)
print(trai_cay)              # ngược thứ tự bảng chữ cái

tuoi = [22, 19, 24, 25, 26, 24, 25, 24]
tuoi.sort()
print(tuoi)   # [19, 22, 24, 24, 24, 25, 25, 26]
tuoi.sort(reverse=True)
print(tuoi)   # [26, 25, 25, 24, 24, 24, 22, 19]
```

- **sorted()**: Trả về danh sách đã sắp xếp mà **không thay đổi** danh sách gốc

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh']
print(sorted(trai_cay))              # bản sao đã sắp xếp
print(trai_cay)                      # danh sách gốc không thay đổi

ds_giam_dan = sorted(trai_cay, reverse=True)
print(ds_giam_dan)
```

🌕 Bạn thật chăm chỉ và đã đạt được khá nhiều. Bạn vừa hoàn thành thử thách ngày 5 và đang tiến thêm 5 bước trên con đường đến sự vĩ đại. Bây giờ hãy làm một số bài tập cho não và cơ bắp của bạn.

## 💻 Bài Tập: Ngày 5

### Bài Tập: Mức 1

1. Khai báo một danh sách rỗng
2. Khai báo một danh sách có hơn 5 phần tử
3. Tìm độ dài của danh sách
4. Lấy phần tử đầu tiên, phần tử giữa và phần tử cuối của danh sách
5. Khai báo danh sách tên `du_lieu_hon_hop`, đặt vào đó (tên, tuổi, chiều cao, tình trạng hôn nhân, địa chỉ)
6. Khai báo biến danh sách tên `cong_ty_it` và gán các giá trị ban đầu là Facebook, Google, Microsoft, Apple, IBM, Oracle và Amazon
7. In danh sách bằng `print()`
8. In số lượng công ty trong danh sách
9. In công ty đầu tiên, công ty giữa và công ty cuối cùng
10. In danh sách sau khi chỉnh sửa một trong các công ty
11. Thêm một công ty IT vào `cong_ty_it`
12. Chèn một công ty IT vào giữa danh sách các công ty
13. Đổi tên một trong các công ty thành chữ hoa (không tính IBM!)
14. Nối `cong_ty_it` bằng chuỗi `'#; '`
15. Kiểm tra xem một công ty nhất định có tồn tại trong danh sách `cong_ty_it` không
16. Sắp xếp danh sách bằng phương thức `sort()`
17. Đảo ngược danh sách theo thứ tự giảm dần bằng `reverse()`
18. Cắt lấy 3 công ty đầu tiên
19. Cắt lấy 3 công ty cuối cùng
20. Cắt lấy công ty hoặc các công ty ở giữa
21. Xóa công ty IT đầu tiên khỏi danh sách
22. Xóa công ty IT hoặc các công ty ở giữa
23. Xóa công ty IT cuối cùng khỏi danh sách
24. Xóa tất cả công ty IT khỏi danh sách
25. Hủy danh sách các công ty IT
26. Nối hai danh sách sau:

    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end  = ['Node', 'Express', 'MongoDB']
    ```

27. Sau khi nối danh sách ở câu 26, hãy sao chép danh sách đã nối vào biến `full_stack`, rồi chèn Python và SQL vào sau Redux.

### Bài Tập: Mức 2

1. Danh sách sau chứa tuổi của 10 học sinh:

```py
tuoi = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

- Sắp xếp danh sách và tìm tuổi nhỏ nhất và lớn nhất
- Thêm tuổi nhỏ nhất và tuổi lớn nhất vào danh sách một lần nữa
- Tìm tuổi trung vị (một phần tử giữa hoặc hai phần tử giữa chia 2)
- Tìm tuổi trung bình (tổng tất cả phần tử chia cho số lượng)
- Tìm khoảng biến thiên (max trừ min)
- So sánh giá trị (min - trung bình) và (max - trung bình), dùng hàm `abs()`

2. Tìm quốc gia ở giữa trong danh sách các quốc gia
3. Chia danh sách quốc gia thành hai nửa bằng nhau, nếu số lẻ thì nửa đầu có thêm một quốc gia
4. `['Trung Quốc', 'Nga', 'Mỹ', 'Phần Lan', 'Thụy Điển', 'Na Uy', 'Đan Mạch']` — Giải nén ba quốc gia đầu và phần còn lại vào biến `bac_au`

🎉 CHÚC MỪNG! 🎉

[<< Ngày 4](../04_Day_Strings/04_strings.md) | [Ngày 6 >>](../06_Day_Tuples/06_tuples.md)
