from core.base_parser import Product

def extract_products(raw_data: list):
    for item in raw_data:
        name = item.get("title", "").strip()
        raw_cost = item.get("cost", "")

        if "не указана" in raw_cost or not raw_cost:
            print(f"⚠️ [ПРОПУСК] Товар '{name}' отфильтрован (нет цены)")
            continue

        clean_cost_str = raw_cost.replace("сум", "").strip()
        try: 
            price = float(clean_cost_str)
        except:
            ValueError
            continue
        
        product = Product(name = name, price = price, category = "Электроника")
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