from data import save_data

# them 1 san pham sao data
def add_product(data):
    
    # nhap vao 
    code = input("Mã sản phẩm: ")
    name = input("Tên sản phẩm: ")
    
    # mapping 
    data["products"].append({
        "code": code,
        "name": name
    })

    # luu
    save_data(data)

    print("Nhập kho thành công")


def del_product(data):
    
    return
