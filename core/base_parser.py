import asyncio

class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Categoty: {self.category} | {self.name} - ${self.price:.1f}"  

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented  
        return self.price < other.price
    

class Base_Parser:
    def __init__(self, category: str):
        self.category = category

    def fetch_raw_data(self) -> list:
        raise NotImplementedError("Метод fetch_raw_data должен быть переопределен!")
    

class DummyParser(Base_Parser):
    super().__init__(category="Электроника")
    
    async def fetch_raw_data(self) -> list:
        await asyncio.sleep(2)
        return [
            {"title": "  iPhone 15 Pro Max  ", "cost": "16000000 сум"},
            {"title": "Чехол для iPhone ", "cost": "150000 сум"},
            {"title": "Сломанный кабель ", "cost": "не указана"}, # Этот должен отфильтроваться!
            {"title": "Xiaomi Redmi Note 13 ", "cost": "3200000 сум"},
        ]
    

if __name__ == "__main__":
    products_list = [
        Product("Laptop", 100.0, "Electronics"),
        Product("Smartphone", 500.0, "Electronics"),
        Product("Headphones", 300.0, "Audio"),
        ]
    
    products_list.sort()
    print("\nSorted products:")
    for product in products_list:        
        print(product)