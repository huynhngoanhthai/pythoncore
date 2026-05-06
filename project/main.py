import json
import os
from datetime import datetime

# File lưu dữ liệu
DATA_FILE = "inventory.json"

def load_data():
    """Tải dữ liệu từ file JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"products": {}, "transactions": []}

def save_data(data):
    """Lưu dữ liệu vào file JSON"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_product(data):
    """Thêm sản phẩm mới"""
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    code = input("Mã sản phẩm: ").strip()
    if not code:
        print("Mã sản phẩm không được để trống!")
        return
    
    if code in data["products"]:
        print(f"Sản phẩm với mã {code} đã tồn tại!")
        return
    
    name = input("Tên sản phẩm: ").strip()
    unit = input("Đơn vị tính (cái, hộp, kg,...): ").strip()
    min_stock = int(input("Tồn kho tối thiểu: ") or "0")
    
    data["products"][code] = {
        "name": name,
        "unit": unit,
        "min_stock": min_stock,
        "quantity": 0
    }
    save_data(data)
    print(f"Đã thêm sản phẩm {name} thành công!")

def import_product(data):
    """Nhập kho"""
    print("\n--- NHẬP KHO ---")
    code = input("Mã sản phẩm: ").strip()
    
    if code not in data["products"]:
        print(f"Sản phẩm có mã {code} không tồn tại!")
        add_new = input("Bạn có muốn thêm sản phẩm mới không? (y/n): ").lower()
        if add_new == 'y':
            add_product(data)
        return
    
    try:
        quantity = int(input("Số lượng nhập: "))
        if quantity <= 0:
            print("Số lượng phải lớn hơn 0!")
            return
        
        price = float(input("Đơn giá nhập: ") or "0")
        supplier = input("Nhà cung cấp: ").strip()
        note = input("Ghi chú: ").strip()
        
        # Cập nhật số lượng tồn
        data["products"][code]["quantity"] += quantity
        
        # Ghi nhận giao dịch
        transaction = {
            "type": "import",
            "code": code,
            "name": data["products"][code]["name"],
            "quantity": quantity,
            "price": price,
            "supplier": supplier,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        data["transactions"].append(transaction)
        save_data(data)
        
        print(f"Đã nhập {quantity} {data['products'][code]['unit']} {data['products'][code]['name']} thành công!")
        
        # Cảnh báo tồn kho
        check_stock_warning(data, code)
        
    except ValueError:
        print("Số lượng hoặc đơn giá không hợp lệ!")

def export_product(data):
    """Xuất kho"""
    print("\n--- XUẤT KHO ---")
    code = input("Mã sản phẩm: ").strip()
    
    if code not in data["products"]:
        print(f"Sản phẩm có mã {code} không tồn tại!")
        return
    
    current_quantity = data["products"][code]["quantity"]
    print(f"Tồn kho hiện tại: {current_quantity} {data['products'][code]['unit']}")
    
    try:
        quantity = int(input("Số lượng xuất: "))
        if quantity <= 0:
            print("Số lượng phải lớn hơn 0!")
            return
        
        if quantity > current_quantity:
            print(f"Không đủ hàng! Tồn kho chỉ còn {current_quantity} {data['products'][code]['unit']}")
            return
        
        reason = input("Lý do xuất (bán, sản xuất, hỏng,...): ").strip()
        recipient = input("Người/Bộ phận nhận: ").strip()
        note = input("Ghi chú: ").strip()
        
        # Cập nhật số lượng tồn
        data["products"][code]["quantity"] -= quantity
        
        # Ghi nhận giao dịch
        transaction = {
            "type": "export",
            "code": code,
            "name": data["products"][code]["name"],
            "quantity": quantity,
            "reason": reason,
            "recipient": recipient,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        data["transactions"].append(transaction)
        save_data(data)
        
        print(f"Đã xuất {quantity} {data['products'][code]['unit']} {data['products'][code]['name']} thành công!")
        
        # Cảnh báo tồn kho
        check_stock_warning(data, code)
        
    except ValueError:
        print("Số lượng không hợp lệ!")

def check_stock_warning(data, code):
    """Kiểm tra và cảnh báo tồn kho dưới mức tối thiểu"""
    product = data["products"][code]
    if product["quantity"] <= product["min_stock"]:
        print(f"\n⚠️ CẢNH BÁO: Sản phẩm {product['name']} tồn kho {product['quantity']} {product['unit']} dưới mức tối thiểu {product['min_stock']} {product['unit']}!")

def view_inventory(data):
    """Xem tồn kho"""
    print("\n--- TỒN KHO HIỆN TẠI ---")
    if not data["products"]:
        print("Chưa có sản phẩm nào!")
        return
    
    print(f"{'Mã SP':<10} {'Tên sản phẩm':<25} {'Tồn kho':<12} {'ĐVT':<8} {'Tồn min':<10} {'Cảnh báo'}")
    print("-" * 80)
    
    for code, info in data["products"].items():
        warning = "⚠️" if info["quantity"] <= info["min_stock"] else ""
        print(f"{code:<10} {info['name']:<25} {info['quantity']:<12} {info['unit']:<8} {info['min_stock']:<10} {warning}")
    
    # Tổng giá trị tồn kho
    total_value = 0
    for code, info in data["products"].items():
        # Lấy giá nhập gần nhất
        last_import_price = get_last_import_price(data, code)
        if last_import_price:
            total_value += info["quantity"] * last_import_price
    
    print(f"\nTổng giá trị tồn kho ước tính: {total_value:,.0f} VND")

def get_last_import_price(data, code):
    """Lấy giá nhập gần nhất của sản phẩm"""
    for trans in reversed(data["transactions"]):
        if trans["type"] == "import" and trans["code"] == code:
            return trans.get("price", 0)
    return 0

def show_menu():
    """Hiển thị menu chính"""
    print("\n" + "=" * 50)
    print("     QUẢN LÝ NHẬP - XUẤT - TỒN KHO")
    print("=" * 50)
    print("1. Thêm sản phẩm mới")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Xem tồn kho")
    print("5. Thoát")
    print("=" * 50)

def main():
    """Hàm chính của chương trình"""
    data = load_data()
    
    while True:
        show_menu()
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == '1':
            add_product(data)
        elif choice == '2':
            import_product(data)
        elif choice == '3':
            export_product(data)
        elif choice == '4':
            view_inventory(data)
        elif choice == '5':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 8!")
        
        input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main()