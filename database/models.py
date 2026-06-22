from database.connection import get_db_connection
from core.base_parser import Product
import asyncio

async def create_tables():
    sql = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,            
        category TEXT NOT NULL,                
        scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    async with get_db_connection() as conn:
        await conn.execute(sql)
        await conn.commit()


            
async def save_product(product: Product):
    sql = "INSERT INTO products (name, price, category) VALUES (?, ?, ?);"
    async with get_db_connection() as conn:
        await conn.execute(sql, (product.name, product.price, product.category))
        await conn.commit()

       

if __name__ == "__main__":
    import asyncio
    
    async def main_test():
        print("🛠️ Инициализация базы данных...")
        await create_tables()
        print("✨ Таблицы готовы!")
        
        # Создаем тестовый объект товара
        test_item = Product(name="iPhone 15 Pro Max", price=16000000.0, category="Смартфоны")
        
        print(f"📥 Пробуем сохранить: {test_item.name}...")
        asyncio.sleep(3)
        await save_product(test_item)
        print("✅ Товар успешно сохранен в SQL!")
        
        # Проверим, что он реально там лежит
        print("\n🔎 Проверяем содержимое базы данных:")
        async with get_db_connection() as conn:
            async with conn.execute("SELECT * FROM products;") as cursor:
                rows = await cursor.fetchall()
                for row in rows:
                    # Помнишь row_factory? Достаем данные по именам колонок!
                    print(f"ID: {row['id']} | Товар: {row['name']} | Цена: {row['price']} сум | Дата: {row['scraped_at']}")

    asyncio.run(main_test())



    