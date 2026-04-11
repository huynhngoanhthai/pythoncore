<div align="center">
  <h1>30 Ngày Học Python: Ngày 7 - Tập Hợp (Sets)</h1>
</div>

[<< Ngày 6](../06_Day_Tuples/06_tuples.md) | [Ngày 8 >>](../08_Day_Dictionaries/08_dictionaries.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Ngày 7](#-ngày-7)
  - [Tập Hợp (Sets)](#tập-hợp-sets)
    - [Tạo Tập Hợp](#tạo-tập-hợp)
    - [Độ Dài Tập Hợp](#độ-dài-tập-hợp)
    - [Truy Cập Phần Tử](#truy-cập-phần-tử)
    - [Kiểm Tra Phần Tử](#kiểm-tra-phần-tử)
    - [Thêm Phần Tử Vào Tập Hợp](#thêm-phần-tử-vào-tập-hợp)
    - [Xóa Phần Tử Khỏi Tập Hợp](#xóa-phần-tử-khỏi-tập-hợp)
    - [Xóa Toàn Bộ Tập Hợp](#xóa-toàn-bộ-tập-hợp)
    - [Hủy Tập Hợp](#hủy-tập-hợp)
    - [Chuyển List Thành Set](#chuyển-list-thành-set)
    - [Hợp Hai Tập Hợp](#hợp-hai-tập-hợp)
    - [Giao Hai Tập Hợp](#giao-hai-tập-hợp)
    - [Tập Con và Tập Cha](#tập-con-và-tập-cha)
    - [Hiệu Hai Tập Hợp](#hiệu-hai-tập-hợp)
    - [Hiệu Đối Xứng](#hiệu-đối-xứng)
    - [Kiểm Tra Tập Hợp Rời Nhau](#kiểm-tra-tập-hợp-rời-nhau)
  - [💻 Bài Tập: Ngày 7](#-bài-tập-ngày-7)

# 📘 Ngày 7

## Tập Hợp (Sets)

Set (Tập hợp) là một tập hợp các phần tử. Định nghĩa tập hợp trong Toán học cũng có thể áp dụng cho Python. Set là tập hợp các phần tử **không có thứ tự, không có chỉ số và không trùng lặp**. Trong Python, set được dùng để lưu trữ các phần tử duy nhất và có thể thực hiện các phép toán tập hợp: **hợp (union)**, **giao (intersection)**, **hiệu (difference)**, **hiệu đối xứng (symmetric difference)**, **tập con (subset)**, **tập cha (superset)** và **tập hợp rời nhau (disjoint set)**.

### Tạo Tập Hợp

Để tạo tập hợp rỗng, dùng hàm `set()`. Dấu ngoặc nhọn `{}` rỗng sẽ tạo **dictionary**, không phải set!

- Tạo tập hợp rỗng:

```py
# cú pháp
tap_hop = set()
```

- Tạo tập hợp có giá trị ban đầu:

```py
# cú pháp
tap_hop = {'pt1', 'pt2', 'pt3', 'pt4'}
```

```py
trai_cay = {'chuối', 'cam', 'xoài', 'chanh'}
```

### Độ Dài Tập Hợp

Dùng hàm `len()` để tìm số phần tử trong tập hợp:

```py
tap_hop = {'pt1', 'pt2', 'pt3', 'pt4'}
len(tap_hop)   # 4
```

```py
trai_cay = {'chuối', 'cam', 'xoài', 'chanh'}
print(len(trai_cay))   # 4
```

### Truy Cập Phần Tử

Không thể truy cập phần tử bằng chỉ số. Chúng ta dùng vòng lặp để duyệt qua các phần tử (sẽ học trong phần vòng lặp).

### Kiểm Tra Phần Tử

Dùng toán tử `in` để kiểm tra phần tử có trong tập hợp không:

```py
tap_hop = {'pt1', 'pt2', 'pt3', 'pt4'}
print('pt3' in tap_hop)   # True
```

```py
trai_cay = {'chuối', 'cam', 'xoài', 'chanh'}
print('xoài' in trai_cay)   # True
```

### Thêm Phần Tử Vào Tập Hợp

Sau khi tạo tập hợp, không thể sửa phần tử có sẵn nhưng có thể thêm phần tử mới.

- Thêm một phần tử bằng `add()`:

```py
tap_hop = {'pt1', 'pt2', 'pt3', 'pt4'}
tap_hop.add('pt5')
```

```py
trai_cay = {'chuối', 'cam', 'xoài', 'chanh'}
trai_cay.add('chanh dây')
print(trai_cay)   # {'chuối', 'cam', 'xoài', 'chanh', 'chanh dây'}
```

- Thêm nhiều phần tử bằng `update()` — nhận đối số là list hoặc tuple:

```py
tap_hop = {'pt1', 'pt2', 'pt3', 'pt4'}
tap_hop.update(['pt5', 'pt6', 'pt7'])
```

```py
trai_cay = {'chuối', 'cam', 'xoài', 'chanh'}
rau_cu   = ('cà chua', 'khoai tây', 'bắp cải', 'hành', 'cà rốt')
trai_cay.update(rau_cu)
print(trai_cay)
```

### Xóa Phần Tử Khỏi Tập Hợp

- `remove()`: Xóa phần tử chỉ định — báo lỗi nếu không tìm thấy
- `discard()`: Xóa phần tử chỉ định — **không báo lỗi** nếu không tìm thấy
- `pop()`: Xóa và trả về một phần tử **ngẫu nhiên**

```py
tap_hop = {'pt1', 'pt2', 'pt3', 'pt4'}
tap_hop.remove('pt2')   # báo lỗi nếu 'pt2' không tồn tại
```

```py
trai_cay = {'chuối', 'cam', 'xoài', 'chanh'}
trai_cay.pop()              # xóa một phần tử ngẫu nhiên

trai_cay2 = {'chuối', 'cam', 'xoài', 'chanh'}
bi_xoa = trai_cay2.pop()    # lấy về phần tử đã bị xóa
print(bi_xoa)
```

### Xóa Toàn Bộ Tập Hợp

Dùng phương thức `clear()` để làm rỗng tập hợp:

```py
tap_hop = {'pt1', 'pt2', 'pt3', 'pt4'}
tap_hop.clear()
```

```py
trai_cay = {'chuối', 'cam', 'xoài', 'chanh'}
trai_cay.clear()
print(trai_cay)   # set()
```

### Hủy Tập Hợp

Dùng từ khóa `del` để hủy hoàn toàn tập hợp:

```py
tap_hop = {'pt1', 'pt2', 'pt3', 'pt4'}
del tap_hop
```

```py
trai_cay = {'chuối', 'cam', 'xoài', 'chanh'}
del trai_cay
```

### Chuyển List Thành Set

Có thể chuyển list thành set và ngược lại. Chuyển list thành set sẽ **loại bỏ các phần tử trùng lặp**, chỉ giữ lại các giá trị duy nhất.

```py
# cú pháp
ds = ['pt1', 'pt2', 'pt3', 'pt4', 'pt1']
tap_hop = set(ds)   # {'pt2', 'pt4', 'pt1', 'pt3'} — thứ tự ngẫu nhiên
```

```py
trai_cay = ['chuối', 'cam', 'xoài', 'chanh', 'cam', 'chuối']
trai_cay = set(trai_cay)   # {'xoài', 'chanh', 'chuối', 'cam'} — đã loại trùng
```

### Hợp Hai Tập Hợp

Dùng `union()` hoặc toán tử `|` — trả về tập hợp mới chứa tất cả phần tử từ cả hai tập hợp:

```py
# cú pháp
tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
tap2 = {'pt5', 'pt6', 'pt7', 'pt8'}
tap3 = tap1.union(tap2)   # hoặc: tap3 = tap1 | tap2
```

```py
trai_cay = {'chuối', 'cam', 'xoài', 'chanh'}
rau_cu   = {'cà chua', 'khoai tây', 'bắp cải', 'hành', 'cà rốt'}
print(trai_cay.union(rau_cu))
# hoặc: print(trai_cay | rau_cu)
```

Dùng `update()` để thêm nội dung của tập hợp khác vào tập hợp hiện tại (thay đổi tại chỗ):

```py
tap1 = {'pt1', 'pt2', 'pt3'}
tap2 = {'pt4', 'pt5', 'pt6'}
tap1.update(tap2)   # nội dung tap2 được thêm vào tap1
```

### Giao Hai Tập Hợp

`intersection()` trả về tập hợp chứa các phần tử **có mặt trong cả hai tập hợp**. Ký hiệu: `&`

```py
# cú pháp
tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
tap2 = {'pt3', 'pt2'}
tap1.intersection(tap2)   # {'pt3', 'pt2'}
# hoặc: tap1 & tap2
```

```py
so_tu_nhien = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
so_chan      = {0, 2, 4, 6, 8, 10}
print(so_tu_nhien.intersection(so_chan))   # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.intersection(dragon))   # {'o', 'n'}
# hoặc: python & dragon
```

### Tập Con và Tập Cha

- `issubset()`: Kiểm tra tập hợp này có là **tập con** của tập hợp kia không
- `issuperset()`: Kiểm tra tập hợp này có là **tập cha** của tập hợp kia không

```py
tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
tap2 = {'pt2', 'pt3'}
print(tap2.issubset(tap1))    # True  — tap2 ⊆ tap1
print(tap1.issuperset(tap2))  # True  — tap1 ⊇ tap2
```

```py
so_tu_nhien = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
so_chan      = {0, 2, 4, 6, 8, 10}
print(so_tu_nhien.issubset(so_chan))    # False — so_tu_nhien là tập cha
print(so_tu_nhien.issuperset(so_chan))  # True

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.issubset(dragon))    # False
```

### Hiệu Hai Tập Hợp

`difference()` trả về các phần tử có trong tập hợp này nhưng **không có trong** tập hợp kia. Ký hiệu: `-`

```py
# cú pháp
tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
tap2 = {'pt2', 'pt3'}
print(tap2.difference(tap1))   # set()        — tap2 - tap1
print(tap1.difference(tap2))   # {'pt1', 'pt4'} — tap1 - tap2
```

```py
so_tu_nhien = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
so_chan      = {0, 2, 4, 6, 8, 10}
print(so_tu_nhien.difference(so_chan))   # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.difference(dragon))   # {'p', 'y', 't'}
print(dragon.difference(python))   # {'d', 'r', 'a', 'g'}
# python - dragon
# dragon - python
```

### Hiệu Đối Xứng

`symmetric_difference()` trả về tập hợp chứa tất cả phần tử từ cả hai tập hợp, **ngoại trừ các phần tử có mặt ở cả hai**. Về toán học: (A\B) ∪ (B\A). Ký hiệu: `^`

```py
# cú pháp
tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
tap2 = {'pt2', 'pt3'}
print(tap2.symmetric_difference(tap1))   # {'pt1', 'pt4'} = tap2 ^ tap1
```

```py
so_tu_nhien = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
mot_so_so   = {1, 2, 3, 4, 5}
print(so_tu_nhien.symmetric_difference(mot_so_so))   # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.symmetric_difference(dragon))   # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon
```

### Kiểm Tra Tập Hợp Rời Nhau

Nếu hai tập hợp không có phần tử chung, gọi là hai tập hợp **rời nhau (disjoint)**. Dùng `isdisjoint()` để kiểm tra:

```py
tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
tap2 = {'pt2', 'pt3'}
print(tap2.isdisjoint(tap1))   # False — có phần tử chung
```

```py
so_chan  = {0, 2, 4, 6, 8}
so_le   = {1, 3, 5, 7, 9}
print(so_chan.isdisjoint(so_le))   # True — không có phần tử chung

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.isdisjoint(dragon))   # False — có phần tử chung {'o', 'n'}
```

🌕 Bạn đang là ngôi sao đang lên. Bạn vừa hoàn thành thử thách ngày 7 và đang tiến thêm 7 bước trên con đường đến sự vĩ đại. Bây giờ hãy làm một số bài tập cho não và cơ bắp của bạn.

## 💻 Bài Tập: Ngày 7

```py
# tập hợp cho bài tập
cong_ty_it = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
tuoi = [22, 19, 24, 25, 26, 24, 25, 24]
```

### Bài Tập: Mức 1

1. Tìm độ dài của tập hợp `cong_ty_it`
2. Thêm 'Twitter' vào `cong_ty_it`
3. Thêm nhiều công ty IT cùng một lúc vào `cong_ty_it`
4. Xóa một trong các công ty khỏi `cong_ty_it`
5. Sự khác biệt giữa `remove()` và `discard()` là gì?

### Bài Tập: Mức 2

1. Hợp A và B
2. Tìm giao của A và B
3. A có phải tập con của B không?
4. A và B có phải là hai tập hợp rời nhau không?
5. Hợp A với B và B với A
6. Hiệu đối xứng giữa A và B là gì?
7. Xóa hoàn toàn cả hai tập hợp

### Bài Tập: Mức 3

1. Chuyển danh sách `tuoi` thành set và so sánh độ dài của list và set — cái nào lớn hơn?
2. Giải thích sự khác nhau giữa các kiểu dữ liệu sau: string, list, tuple và set
3. _Tôi là giáo viên và tôi yêu thích truyền cảm hứng và dạy học cho mọi người._ Có bao nhiêu từ **duy nhất** được dùng trong câu? Dùng phương thức split và set để lấy các từ duy nhất.

🎉 CHÚC MỪNG! 🎉

[<< Ngày 6](../06_Day_Tuples/06_tuples.md) | [Ngày 8 >>](../08_Day_Dictionaries/08_dictionaries.md)
