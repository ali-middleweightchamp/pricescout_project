from core.base_parser import Product

def extract_products(raw_data: list):
    for item in raw_data:
        name = item.get("title")
        fake_price = float(item.get("id", 0) * 100000)
        
        product = Product(name = name, price = fake_price, category = "Тест")
        yield product

if __name__ == "__main__":
    print("🚀 Тестируем фильтрацию данных (processing.py)...")
    
    # Имитируем грязный ответ от fetcher.py
    mock_raw_data = [
        {"userId": 1, "id": 1, "title": "iPhone 15 Pro", "body": "bla bla"},
        {"userId": 1, "id": 2, "title": "Samsung S24 Ultra", "body": "bla bla"},
    ]
    
    # Получаем генератор
    products_generator = extract_products(mock_raw_data)
    
    print("\n🎯 Результат чистки:")
    for prod in products_generator:
        print(f"Товар: {prod.name} | Цена: {prod.price} сум")