<div align="center">
  <h1> 30 Ngày Học Python: Ngày 11 - Hàm</h1>
</div>

[<< Ngày 10](../10_Day_Loops/10_loops.md) | [Ngày 12 >>](../12_Day_Modules/12_modules.md)

- [📘 Ngày 11](#-ngày-11)
  - [Hàm](#hàm)
    - [Định Nghĩa Hàm](#định-nghĩa-hàm)
    - [Khai Báo và Gọi Hàm](#khai-báo-và-gọi-hàm)
    - [Hàm Không Có Tham Số](#hàm-không-có-tham-số)
    - [Hàm Có Giá Trị Trả Về - Phần 1](#hàm-có-giá-trị-trả-về---phần-1)
    - [Hàm Có Tham Số](#hàm-có-tham-số)
    - [Truyền Đối Số Theo Tên và Giá Trị](#truyền-đối-số-theo-tên-và-giá-trị)
    - [Hàm Có Giá Trị Trả Về - Phần 2](#hàm-có-giá-trị-trả-về---phần-2)
    - [Hàm Với Tham Số Mặc Định](#hàm-với-tham-số-mặc-định)
    - [Số Lượng Đối Số Tùy Ý](#số-lượng-đối-số-tùy-ý)
    - [Tham Số Mặc Định và Tham Số Tùy Ý Trong Hàm](#tham-số-mặc-định-và-tham-số-tùy-ý-trong-hàm)
    - [Hàm Là Tham Số Của Hàm Khác](#hàm-là-tham-số-của-hàm-khác)
  - [Lời Chứng Thực](#lời-chứng-thực)
  - [💻 Bài Tập: Ngày 11](#-bài-tập-ngày-11)
    - [Bài Tập: Cấp Độ 1](#bài-tập-cấp-độ-1)
    - [Bài Tập: Cấp Độ 2](#bài-tập-cấp-độ-2)
    - [Bài Tập: Cấp Độ 3](#bài-tập-cấp-độ-3)

# 📘 Ngày 11

## Hàm

Cho đến nay chúng ta đã thấy nhiều hàm dựng sẵn của Python. Trong phần này, chúng ta sẽ tập trung vào các hàm tự định nghĩa. Hàm là gì? Trước khi bắt đầu viết hàm, hãy cùng tìm hiểu hàm là gì và tại sao chúng ta cần đến chúng.

### Định Nghĩa Hàm

Hàm là một khối code có thể tái sử dụng, hoặc là các câu lệnh lập trình được thiết kế để thực hiện một tác vụ nhất định. Để định nghĩa hoặc khai báo một hàm, Python cung cấp từ khóa _def_. Dưới đây là cú pháp để định nghĩa một hàm. Khối code bên trong hàm chỉ được thực thi khi hàm được gọi hoặc kích hoạt.

### Khai Báo và Gọi Hàm

Khi chúng ta tạo một hàm, ta gọi đó là khai báo hàm. Khi bắt đầu sử dụng nó, ta gọi đó là _gọi_ hoặc _kích hoạt_ hàm. Hàm có thể được khai báo có hoặc không có tham số.

```py
# cú pháp
# Khai báo hàm
def tên_hàm():
    các_câu_lệnh
    các_câu_lệnh
# Gọi hàm
tên_hàm()
```

### Hàm Không Có Tham Số

Hàm có thể được khai báo mà không cần tham số.

**Ví dụ:**

```py
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name() # gọi hàm

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### Hàm Có Giá Trị Trả Về - Phần 1

Hàm trả về giá trị bằng câu lệnh _return_. Nếu hàm không có câu lệnh return, nó sẽ trả về None. Hãy viết lại các hàm trên dùng return. Từ bây giờ, chúng ta sẽ nhận giá trị từ hàm khi gọi và in nó ra.

```py
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### Hàm Có Tham Số

Trong hàm, chúng ta có thể truyền các kiểu dữ liệu khác nhau (số, chuỗi, boolean, danh sách, tuple, từ điển hoặc tập hợp) làm tham số.

- Một Tham Số: Nếu hàm có một tham số, chúng ta phải gọi hàm đó với một đối số tương ứng.

```py
  # cú pháp
  # Khai báo hàm
  def tên_hàm(tham_số):
    các_câu_lệnh
    các_câu_lệnh
  # Gọi hàm
  print(tên_hàm(đối_số))
```

**Ví dụ:**

```py
def greetings(name):
    message = name + ', chào mừng đến với Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- Hai Tham Số: Hàm có thể có hoặc không có tham số. Hàm cũng có thể có hai tham số trở lên. Nếu hàm có các tham số, chúng ta cần gọi nó với các đối số tương ứng. Ví dụ hàm với hai tham số:

```py
  # cú pháp
  # Khai báo hàm
  def tên_hàm(tham_số1, tham_số2):
    các_câu_lệnh
    các_câu_lệnh
  # Gọi hàm
  print(tên_hàm(đối_số1, đối_số2))
```

**Ví dụ:**

```py
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Họ tên đầy đủ: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print('Tổng hai số: ', sum_two_numbers(1, 9))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print('Tuổi: ', calculate_age(2021, 1819))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N' # giá trị phải được chuyển sang chuỗi trước
    return weight
print('Trọng lượng của vật thể tính bằng Newton: ', weight_of_object(100, 9.81))
```

### Truyền Đối Số Theo Tên và Giá Trị

Nếu truyền đối số theo tên và giá trị, thứ tự của các đối số sẽ không quan trọng.

```py
# cú pháp
# Khai báo hàm
def tên_hàm(tham_số1, tham_số2):
    các_câu_lệnh
    các_câu_lệnh
# Gọi hàm
print(tên_hàm(tham_số1 = 'John', tham_số2 = 'Doe')) # thứ tự đối số không quan trọng ở đây
```

**Ví dụ:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Thứ tự không quan trọng
```

### Hàm Có Giá Trị Trả Về - Phần 2

Nếu không trả về giá trị, hàm mặc định sẽ trả về _None_. Để trả về giá trị, ta dùng từ khóa _return_ theo sau là biến cần trả về. Hàm có thể trả về bất kỳ kiểu dữ liệu nào.

- Trả về chuỗi:
**Ví dụ:**

```py
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

- Trả về số:

**Ví dụ:**

```py
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Tuổi: ', calculate_age(2019, 1819))
```

- Trả về boolean:

**Ví dụ:**

```py
def is_even(n):
    if n % 2 == 0:
        return True    # return dừng thực thi thêm của hàm, tương tự break
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- Trả về danh sách:

**Ví dụ:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### Hàm Với Tham Số Mặc Định

Đôi khi chúng ta truyền giá trị mặc định cho tham số khi gọi hàm. Nếu không truyền đối số khi gọi hàm, các giá trị mặc định sẽ được dùng.

```py
# cú pháp
# Khai báo hàm
def tên_hàm(tham_số = giá_trị):
    các_câu_lệnh
    các_câu_lệnh
# Gọi hàm
tên_hàm()
tên_hàm(đối_số)
```

**Ví dụ:**

```py
def greetings(name = 'Peter'):
    message = name + ', chào mừng đến với Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name(first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age(birth_year, current_year = 2021):
    age = current_year - birth_year
    return age
print('Tuổi: ', calculate_age(1821))

def weight_of_object(mass, gravity = 9.81):
    weight = str(mass * gravity) + ' N' # giá trị phải được chuyển sang chuỗi trước
    return weight
print('Trọng lượng của vật thể tính bằng Newton: ', weight_of_object(100)) # 9.81 - gia tốc trọng trường trung bình trên bề mặt Trái Đất
print('Trọng lượng của vật thể tính bằng Newton: ', weight_of_object(100, 1.62)) # gia tốc trọng trường trên bề mặt Mặt Trăng
```

### Số Lượng Đối Số Tùy Ý

Nếu không biết trước số lượng đối số truyền vào hàm, chúng ta có thể tạo hàm nhận số lượng đối số tùy ý bằng cách thêm dấu \* trước tên tham số.

```py
# cú pháp
# Khai báo hàm
def tên_hàm(*args):
    các_câu_lệnh
    các_câu_lệnh
# Gọi hàm
tên_hàm(tham_số1, tham_số2, tham_số3, ...)
```

**Ví dụ:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # tương đương total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### Tham Số Mặc Định và Tham Số Tùy Ý Trong Hàm

```py
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```

### Giải Nén Từ Điển (Dictionary Unpacking)

Bạn có thể gọi hàm có đối số theo tên bằng cách truyền một từ điển có các khóa trùng với tên tham số. Sử dụng toán tử `**` để làm điều này.

```py
# Định nghĩa hàm nhận hai đối số: 'name' và 'location'
def greet(name, location):
    # In ra thông điệp chào hỏi dùng các đối số được cung cấp
    print("Xin chào", name, "thời tiết ở", location, "thế nào?")

# Gọi hàm dùng đối số theo tên
greet(name="Alice", location="New York")
# Kết quả: Xin chào Alice thời tiết ở New York thế nào?

# Tạo từ điển với các khóa khớp với tên tham số của hàm
my_dict = {"name": "Alice", "location": "New York"}

# Gọi hàm dùng giải nén từ điển
greet(**my_dict)
# Toán tử ** giải nén từ điển, truyền các cặp khóa-giá trị
# làm đối số theo tên cho hàm.
# Kết quả: Xin chào Alice thời tiết ở New York thế nào?
```

### Số Lượng Đối Số Theo Tên Tùy Ý

Bạn cũng có thể định nghĩa hàm nhận số lượng đối số theo tên tùy ý.

```py
def arbitrary_named_args(**args):
    print("Tôi nhận được số lượng đối số tùy ý, tổng cộng", len(args))
    print("Chúng được cung cấp dưới dạng từ điển trong hàm:", type(args))
    print("Hãy in chúng ra:")
    for k, v in args.items():
        print(" * khóa:", k, "giá trị:", v)
```

Nhìn chung, hãy tránh dùng cách này trừ khi cần thiết, vì nó khiến khó hiểu hàm chấp nhận và làm gì.

### Hàm Là Tham Số Của Hàm Khác

```py
# Bạn có thể truyền hàm như là tham số
def square_number(n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 Bạn đã đạt được khá nhiều thứ rồi đấy. Tiếp tục nào! Bạn vừa hoàn thành thử thách ngày 11 và đang tiến thêm 11 bước trên con đường đến thành công. Bây giờ hãy làm một số bài tập để rèn luyện trí não và đôi tay nhé.

## Lời Chứng Thực

Đây là lúc bày tỏ suy nghĩ của bạn về Tác Giả và 30DaysOfPython. Bạn có thể để lại lời chứng thực tại [đây](https://testimonial-s3sw.onrender.com/).

## 💻 Bài Tập: Ngày 11

### Bài Tập: Cấp Độ 1

1. Khai báo hàm _add_two_numbers_. Hàm nhận hai tham số và trả về tổng của chúng.
2. Diện tích hình tròn được tính theo công thức: diện_tích = π x r x r. Viết hàm tính _area_of_circle_.
3. Viết hàm tên _add_all_nums_ nhận số lượng đối số tùy ý và tính tổng tất cả các đối số đó. Kiểm tra xem tất cả phần tử trong danh sách có phải là kiểu số không. Nếu không, hãy thông báo lỗi hợp lý.
4. Nhiệt độ °C có thể chuyển sang °F theo công thức: °F = (°C x 9/5) + 32. Viết hàm chuyển đổi °C sang °F, đặt tên là _convert_celsius_to_fahrenheit_.
5. Viết hàm tên _check_season_, nhận tham số là tháng và trả về mùa: Thu, Đông, Xuân hay Hạ.
6. Viết hàm _calculate_slope_ trả về độ dốc của một phương trình tuyến tính.
7. Phương trình bậc hai được tính theo công thức: ax² + bx + c = 0. Viết hàm tính tập nghiệm của phương trình bậc hai, đặt tên là _solve_quadratic_eqn_.
8. Khai báo hàm tên _print_list_. Hàm nhận một danh sách làm tham số và in ra từng phần tử của danh sách đó.
9. Khai báo hàm tên _reverse_list_. Hàm nhận một mảng làm tham số và trả về mảng đó theo thứ tự ngược lại (dùng vòng lặp).

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]
```

10. Khai báo hàm tên _capitalize_list_items_. Hàm nhận một danh sách làm tham số và trả về danh sách các phần tử đã được viết hoa chữ cái đầu.
11. Khai báo hàm tên _add_item_. Hàm nhận một danh sách và một phần tử làm tham số. Trả về danh sách với phần tử được thêm vào cuối.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
```

12. Khai báo hàm tên _remove_item_. Hàm nhận một danh sách và một phần tử làm tham số. Trả về danh sách sau khi đã xóa phần tử đó.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. Khai báo hàm tên _sum_of_numbers_. Hàm nhận một số nguyên và tính tổng tất cả các số từ 0 đến số đó.

```py
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

14. Khai báo hàm tên _sum_of_odds_. Hàm nhận một số nguyên và tính tổng tất cả các số lẻ trong khoảng đó.
15. Khai báo hàm tên _sum_of_even_. Hàm nhận một số nguyên và tính tổng tất cả các số chẵn trong khoảng đó.

### Bài Tập: Cấp Độ 2

1. Khai báo hàm tên _evens_and_odds_. Hàm nhận một số nguyên dương làm tham số và đếm số lượng số chẵn và lẻ trong khoảng đó.

```py
    print(evens_and_odds(100))
    # Số lượng số lẻ là 50.
    # Số lượng số chẵn là 51.
```

2. Gọi hàm của bạn là _factorial_, nhận một số nguyên và trả về giai thừa của số đó.
3. Gọi hàm của bạn là _is_empty_, nhận một tham số và kiểm tra xem nó có rỗng hay không.
4. Viết các hàm khác nhau nhận danh sách làm đầu vào. Các hàm đó nên tính: calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (độ lệch chuẩn).
5. Viết hàm tên _greet_ nhận một đối số mặc định là _name_. Nếu không có đối số nào được cung cấp, in ra "Xin chào, Khách!"; ngược lại, chào người dùng theo tên.

```py
    greet()
    # "Xin chào, Khách!"
    greet("Alice")
    # "Xin chào, Alice!"
```

6. Tạo hàm tên _show_args_ nhận số lượng đối số theo tên tùy ý và in ra tên cùng giá trị của chúng.
   ```py
   show_args(name="Alice", age=30, city="New York")
   # Nhận được: name: Alice, age: 30, city: New York
   show_args(name="Bob", pet="Fluffy, the bunny")
   # Nhận được: name: Bob, pet: Fluffy, the bunny
   ```

### Bài Tập: Cấp Độ 3

1. Viết hàm tên _is_prime_ để kiểm tra xem một số có phải số nguyên tố không.
2. Viết hàm kiểm tra xem tất cả các phần tử trong danh sách có là duy nhất không.
3. Viết hàm kiểm tra xem tất cả các phần tử trong danh sách có cùng kiểu dữ liệu không.
4. Viết hàm kiểm tra xem biến được cung cấp có phải là tên biến Python hợp lệ không.
5. Vào thư mục data và truy cập file countries-data.py.

- Tạo hàm tên _most_spoken_languages_ (ngôn ngữ được nói nhiều nhất) trên thế giới. Hàm trả về 10 hoặc 20 ngôn ngữ được nói nhiều nhất theo thứ tự giảm dần.
- Tạo hàm tên _most_populated_countries_ (quốc gia đông dân nhất). Hàm trả về 10 hoặc 20 quốc gia đông dân nhất theo thứ tự giảm dần.

🎉 CHÚC MỪNG! 🎉

[<< Ngày 10](../10_Day_Loops/10_loops.md) | [Ngày 12 >>](../12_Day_Modules/12_modules.md)
