from data import load_data
from product import add_product,del_product,update_product
from inventory import import_product, export_product, view_inventory

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
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5!")
    
    input("\nNhấn Enter để tiếp tục...")
