<div align="center">
  <h1>30 Ngày Học Python: Ngày 2 - Biến và Hàm Có Sẵn</h1>
</div>

[<< Ngày 1](../readme.md) | [Ngày 3 >>](../03_Day_Operators/03_operators.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Ngày 2](#-ngày-2)
  - [Hàm Có Sẵn](#hàm-có-sẵn)
  - [Biến](#biến)
    - [Khai Báo Nhiều Biến Trên Một Dòng](#khai-báo-nhiều-biến-trên-một-dòng)
  - [Kiểu Dữ Liệu](#kiểu-dữ-liệu)
  - [Kiểm Tra Kiểu Dữ Liệu và Chuyển Đổi](#kiểm-tra-kiểu-dữ-liệu-và-chuyển-đổi)
  - [Số](#số)
  - [💻 Bài Tập - Ngày 2](#-bài-tập---ngày-2)
    - [Bài Tập: Mức 1](#bài-tập-mức-1)
    - [Bài Tập: Mức 2](#bài-tập-mức-2)

# 📘 Ngày 2

## Hàm Có Sẵn

Trong Python, chúng ta có rất nhiều hàm có sẵn (built-in functions). Các hàm có sẵn có thể dùng ở bất kỳ đâu — tức là bạn có thể sử dụng chúng mà không cần import hay cấu hình thêm gì. Một số hàm có sẵn phổ biến nhất trong Python là: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, _open()_, _file()_, _help()_, và _dir()_. Trong bảng dưới đây bạn sẽ thấy danh sách đầy đủ các hàm có sẵn của Python được lấy từ [tài liệu Python](https://docs.python.org/3/library/functions.html).

![Hàm Có Sẵn](../images/builtin-functions.png)

Hãy mở Python shell và bắt đầu sử dụng một số hàm có sẵn phổ biến nhất.

![Hàm Có Sẵn](../images/builtin-functions_practice.png)

Hãy thực hành thêm bằng cách sử dụng các hàm có sẵn khác nhau.

![Hàm Help và Dir](../images/help_and_dir_builtin.png)

Như bạn có thể thấy từ terminal trên, Python có các từ khóa dành riêng (reserved words). Chúng ta không dùng các từ khóa dành riêng để khai báo biến hoặc hàm. Chúng ta sẽ đề cập đến biến trong phần tiếp theo.

Tôi tin rằng đến đây bạn đã quen với các hàm có sẵn. Hãy thực hành thêm một lần nữa với hàm có sẵn rồi chuyển sang phần tiếp theo.

![Min Max Sum](../images/builtin-functional-final.png)

## Biến

Biến lưu trữ dữ liệu trong bộ nhớ máy tính. Nên dùng các tên biến có ý nghĩa (mnemonic variables) trong nhiều ngôn ngữ lập trình. Tên biến có ý nghĩa là tên biến dễ nhớ và dễ liên tưởng. Biến tham chiếu đến một địa chỉ bộ nhớ nơi dữ liệu được lưu trữ.
Không được dùng số ở đầu, ký tự đặc biệt hay dấu gạch ngang khi đặt tên biến. Biến có thể có tên ngắn (như x, y, z), nhưng tên mô tả hơn (ten, ho, tuoi, quoc_gia) được khuyến khích sử dụng.

Quy Tắc Đặt Tên Biến Python:

- Tên biến phải bắt đầu bằng một chữ cái hoặc ký tự gạch dưới (_)
- Tên biến không được bắt đầu bằng số
- Tên biến chỉ có thể chứa ký tự chữ-số và gạch dưới (A-z, 0-9 và \_)
- Tên biến phân biệt chữ hoa/thường (ten, Ten, TEN và TEN là các biến khác nhau)

Một số ví dụ về tên biến hợp lệ:

```shell
ten
ho
tuoi
quoc_gia
thanh_pho
ten_dem
ho_ten
thu_do
_if # nếu muốn dùng từ khóa dành riêng làm biến
nam_2021
nam2021
nam_hien_tai_2021
nam_sinh
so1
so2
```

Tên biến không hợp lệ:

```shell
ho-ten
ho@ten
ho$ten
so-1
1so
```

Chúng ta sẽ dùng quy ước đặt tên biến Python chuẩn được nhiều lập trình viên Python áp dụng. Lập trình viên Python dùng quy ước đặt tên snake_case (viết thường, dùng gạch dưới). Chúng ta dùng ký tự gạch dưới sau mỗi từ cho biến có nhiều hơn một từ (ví dụ: ten_dem, ho_ten, toc_do_quay_dong_co). Ví dụ dưới đây minh họa cách đặt tên biến chuẩn, gạch dưới bắt buộc khi tên biến có nhiều hơn một từ.

Khi chúng ta gán một kiểu dữ liệu nhất định cho một biến, đó gọi là khai báo biến. Ví dụ trong đoạn mã dưới đây, tên của tôi được gán vào biến ten. Dấu bằng là toán tử gán. Gán nghĩa là lưu dữ liệu vào biến. Dấu bằng trong Python không có nghĩa là bằng nhau như trong Toán học.

_Ví dụ:_

```py
# Biến trong Python
ten = 'Nguyễn Văn An'
ho = 'Nguyễn'
quoc_gia = 'Việt Nam'
thanh_pho = 'Hà Nội'
tuoi = 25
da_lap_gia_dinh = False
ky_nang = ['HTML', 'CSS', 'JS', 'React', 'Python']
thong_tin_ca_nhan = {
   'ten': 'Nguyễn Văn An',
   'ho': 'Nguyễn',
   'quoc_gia': 'Việt Nam',
   'thanh_pho': 'Hà Nội'
   }
```

Hãy dùng hàm có sẵn _print()_ và _len()_. Hàm print có thể nhận số lượng đối số không giới hạn. Đối số là giá trị chúng ta có thể truyền vào hoặc đặt bên trong dấu ngoặc của hàm, xem ví dụ bên dưới.

**Ví dụ:**

```py
print('Xin chào, Thế giới!') # Văn bản Xin chào, Thế giới! là đối số
print('Xin chào',',', 'Thế giới','!') # có thể nhận nhiều đối số, đã truyền vào bốn đối số
print(len('Xin chào, Thế giới!')) # chỉ nhận một đối số
```

Hãy in ra và tìm độ dài của các biến đã khai báo ở trên:

**Ví dụ:**

```py
# In ra các giá trị được lưu trong biến

print('Tên:', ten)
print('Độ dài tên:', len(ten))
print('Họ:', ho)
print('Độ dài họ:', len(ho))
print('Quốc gia:', quoc_gia)
print('Thành phố:', thanh_pho)
print('Tuổi:', tuoi)
print('Đã lập gia đình:', da_lap_gia_dinh)
print('Kỹ năng:', ky_nang)
print('Thông tin cá nhân:', thong_tin_ca_nhan)
```

### Khai Báo Nhiều Biến Trên Một Dòng

Có thể khai báo nhiều biến trong một dòng:

**Ví dụ:**

```py
ten, ho, quoc_gia, tuoi, da_lap_gia_dinh = 'Nguyễn Văn An', 'Nguyễn', 'Việt Nam', 25, False

print(ten, ho, quoc_gia, tuoi, da_lap_gia_dinh)
print('Tên:', ten)
print('Họ:', ho)
print('Quốc gia:', quoc_gia)
print('Tuổi:', tuoi)
print('Đã lập gia đình:', da_lap_gia_dinh)
```

Lấy đầu vào từ người dùng bằng hàm có sẵn _input()_. Hãy gán dữ liệu nhận được từ người dùng vào các biến ten và tuoi.

**Ví dụ:**

```py
ten = input('Tên của bạn là gì: ')
tuoi = input('Bạn bao nhiêu tuổi? ')

print(ten)
print(tuoi)
```

## Kiểu Dữ Liệu

Trong Python có nhiều kiểu dữ liệu. Để xác định kiểu dữ liệu, chúng ta dùng hàm có sẵn _type_. Tôi muốn bạn tập trung hiểu thật tốt các kiểu dữ liệu khác nhau. Khi nói đến lập trình, tất cả đều xoay quanh kiểu dữ liệu. Tôi đã giới thiệu kiểu dữ liệu ngay từ đầu và nó xuất hiện lại ở đây, vì mọi chủ đề đều liên quan đến kiểu dữ liệu. Chúng ta sẽ đề cập kiểu dữ liệu chi tiết hơn trong các phần tương ứng.

## Kiểm Tra Kiểu Dữ Liệu và Chuyển Đổi

- Kiểm tra kiểu dữ liệu: Để kiểm tra kiểu dữ liệu của một dữ liệu/biến nhất định, chúng ta dùng hàm _type_

  **Ví dụ:**

```py
# Các kiểu dữ liệu Python khác nhau
# Hãy khai báo biến với nhiều kiểu dữ liệu khác nhau

ten = 'Nguyễn Văn An'    # str
ho = 'Nguyễn'            # str
quoc_gia = 'Việt Nam'    # str
thanh_pho = 'Hà Nội'     # str
tuoi = 25                # int

# In ra các kiểu dữ liệu
print(type('Nguyễn Văn An'))     # str
print(type(ten))                 # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'ten': 'An'}))       # dict
print(type((1, 2)))              # tuple
print(type(zip([1,2],[3,4])))    # zip
```

- Chuyển đổi kiểu (Casting): Chuyển đổi từ kiểu dữ liệu này sang kiểu dữ liệu khác. Chúng ta dùng _int()_, _float()_, _str()_, _list_, _set_.
  Khi thực hiện phép toán số học, chuỗi số phải được chuyển đổi thành int hoặc float trước, nếu không sẽ trả về lỗi. Nếu ghép nối một số với chuỗi, số phải được chuyển đổi thành chuỗi trước. Chúng ta sẽ nói về ghép nối chuỗi trong phần Chuỗi.

  **Ví dụ:**

```py
# int sang float
so_nguyen = 10
print('so_nguyen', so_nguyen)        # 10
so_thuc = float(so_nguyen)
print('so_thuc:', so_thuc)           # 10.0

# float sang int
trong_luc = 9.81
print(int(trong_luc))                # 9

# int sang str
so_nguyen = 10
print(so_nguyen)                     # 10
so_chuoi = str(so_nguyen)
print(so_chuoi)                      # '10'

# str sang int hoặc float
chuoi_so = '10.6'
so_thuc = float(chuoi_so)       # Chuyển chuỗi sang float trước
so_nguyen = int(so_thuc)        # Sau đó chuyển float sang int
print('so_nguyen', int(chuoi_so))    # 10
print('so_thuc', float(chuoi_so))    # 10.6

# str sang list
ten = 'Nguyễn'
print(ten)                           # 'Nguyễn'
ten_thanh_danh_sach = list(ten)
print(ten_thanh_danh_sach)           # ['N', 'g', 'u', 'y', 'ễ', 'n']
```

## Số

Các kiểu dữ liệu số trong Python:

1. Số nguyên (Integer): Số nguyên (âm, không và dương)
   Ví dụ:
   ... -3, -2, -1, 0, 1, 2, 3 ...

2. Số thực (Floating Point Numbers - Số thập phân)
   Ví dụ:
   ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3. Số phức (Complex Numbers)
   Ví dụ:
   1 + j, 2 + 4j, 1 - 1j

🌕 Bạn thật tuyệt vời. Bạn vừa hoàn thành thử thách ngày 2 và đang tiến thêm hai bước trên con đường đến sự vĩ đại. Bây giờ hãy làm một số bài tập cho não và cơ bắp của bạn.

## 💻 Bài Tập - Ngày 2

### Bài Tập: Mức 1

1. Trong thư mục 30DaysOfPython tạo một thư mục tên day_2. Trong thư mục này tạo file tên variables.py
2. Viết chú thích Python với nội dung 'Ngày 2: 30 Ngày học lập trình Python'
3. Khai báo biến tên và gán giá trị cho nó
4. Khai báo biến họ và gán giá trị cho nó
5. Khai báo biến họ_tên và gán giá trị cho nó
6. Khai báo biến quoc_gia và gán giá trị cho nó
7. Khai báo biến thanh_pho và gán giá trị cho nó
8. Khai báo biến tuoi và gán giá trị cho nó
9. Khai báo biến nam và gán giá trị cho nó
10. Khai báo biến da_lap_gia_dinh và gán giá trị cho nó
11. Khai báo biến la_dung và gán giá trị cho nó
12. Khai báo biến den_dang_bat và gán giá trị cho nó
13. Khai báo nhiều biến trên cùng một dòng

### Bài Tập: Mức 2

1. Kiểm tra kiểu dữ liệu của tất cả các biến của bạn bằng hàm có sẵn type()
2. Dùng hàm có sẵn _len()_, tìm độ dài tên của bạn
3. So sánh độ dài tên và họ của bạn
4. Khai báo 5 là so_mot và 4 là so_hai
5. Cộng so_mot và so_hai và gán giá trị vào biến tong
6. Trừ so_hai từ so_mot và gán giá trị vào biến hieu
7. Nhân so_hai và so_mot và gán giá trị vào biến tich
8. Chia so_mot cho so_hai và gán giá trị vào biến thuong
9. Dùng phép chia lấy dư để tính so_hai chia cho so_mot và gán giá trị vào biến du
10. Tính so_mot lũy thừa so_hai và gán giá trị vào biến luy_thua
11. Tìm phép chia lấy phần nguyên của so_mot cho so_hai và gán vào biến chia_nguyen
12. Bán kính của một hình tròn là 30 mét.
    1. Tính diện tích hình tròn và gán vào biến _dien_tich_hinh_tron_
    2. Tính chu vi hình tròn và gán vào biến _chu_vi_hinh_tron_
    3. Nhận bán kính từ người dùng và tính diện tích
13. Dùng hàm input có sẵn để lấy tên, họ, quốc gia và tuổi từ người dùng rồi lưu vào các biến tương ứng
14. Chạy help('keywords') trong Python shell hoặc trong file của bạn để kiểm tra các từ khóa dành riêng của Python

🎉 CHÚC MỪNG! 🎉

[<< Ngày 1](../readme.md) | [Ngày 3 >>](../03_Day_Operators/03_operators.md)
