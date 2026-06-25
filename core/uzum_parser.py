import asyncio
import aiohttp
from core.base_parser import Base_Parser

class UzumParser(Base_Parser):
    def __init__(self):
        super().__init__(category="Электроника")
        # Открытый тестовый API с реальными товарами
        self.url = "https://fakestoreapi.com/products/category/electronics"

    async def fetch_raw_data(self):
        headers = {"Accept": "application/json"}

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.url, headers=headers, timeout=10) as response:
                    if response.status != 200:
                        print(f"❌ Ошибка API! Статус: {response.status}")
                        return []
                    
                    data = await response.json()
                    
                    # Магия адаптации: превращаем ключи API ('price') в 'sellPrice', 
                    # чтобы твой extract_products в modules/processing.py не пришлось менять!
                    adapted_products = []
                    for item in data:
                        adapted_products.append({
                            "title": item.get("title"),
                            "sellPrice": item.get("price")  # подменяем ключ на тот, что ищет фильтр
                        })
                    
                    return adapted_products
                    
            except Exception as e:
                print(f"❌ Ошибка сети: {e}")
                return []