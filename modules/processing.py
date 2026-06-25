from core.base_parser import Product

def extract_products(raw_data: list):
    for item in raw_data:
        name = item.get("title", "").strip()
        sellPrice = item.get("sellPrice", "")

        if not sellPrice or sellPrice <= 0:
            print(f"⚠️ [ПРОПУСК] Товар '{name}' отфильтрован (нет цены)")
            continue

        try: 
            price = float(sellPrice)
        except ValueError:
            continue
        
        product = Product(name = name, price = price, category = "Электроника")
        yield product

