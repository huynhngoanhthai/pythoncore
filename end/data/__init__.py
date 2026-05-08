import json
import os

DATA_FILE = "data/data.json"

def load_data():
    """Tải dữ liệu từ file JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "products": [], 
        "transactions": [],   
        "productMaxId": 0,
        "transactionMaxId": 0
    }

def save_data(data):
    """Lưu dữ liệu vào file JSON"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)