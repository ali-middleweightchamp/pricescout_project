class Product:
    def __init__(self, name: str, price: float, category: str):
        """
        Конструктор класса. Срабатывает, когда мы пишем Product(...)
        self — это указатель на конкретный создаваемый товар (например, на айфон).
        """
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        """
        Магический метод для превращения объекта в текст.
        Если мы его не напишем, print(product) выведет мусор в виде адреса памяти.
        С ним — выдаст красивую строку.
        """
        return f"[{self.category}] {self.name} — ${self.price}"

    def __lt__(self, other):
        """
        Магический метод 'меньше' (<). 
        Учит Python сравнивать товары между собой по цене.
        self — текущий товар, other — тот, с которым сравниваем.
        """
        if not isinstance(other, Product):
            # Если программист случайно попытается сравнить товар со строкой или числом,
            # мы вежливо откажемся, чтобы не сломать программу скрытой ошибкой.
            return NotImplemented
        return self.price < other.price


# --- БЛОК ТЕСТИРОВАНИЯ ---
# Этот код сработает, только если запустить этот файл напрямую.
if __name__ == "__main__":
    print("🚀 Тестируем наш ООП-фундамент:\n")
    
    # Создаем три объекта товара (вразброс по ценам)
    p1 = Product("iPhone 15 Pro", 1200.0, "Смартфоны")
    p2 = Product("iPhone 14", 700.0, "Смартфоны")
    p3 = Product("Samsung S24", 1000.0, "Смартфоны")
    
    # 1. Проверяем, как работает __str__
    print("Вывод товара через print():")
    print(p1)  
    
    # 2. Проверяем, как работает __lt__ (сравнение)
    print("\nПроверяем сравнение:")
    print(f"iPhone 14 дешевле чем iPhone 15 Pro? -> {p2 < p1}")  # Ожидаем True
    
    # 3. Проверяем магию автоматической сортировки Python
    products_list = [p1, p2, p3]
    products_list.sort()  # Python сам вызовет метод __lt__ для каждого товара!
    
    print("\nТовары после автоматической сортировки (по возрастанию цены):")
    for product in products_list:
        print(product)