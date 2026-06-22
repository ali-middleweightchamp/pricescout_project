from database.connection import get_db_connection
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
            
       

if __name__ == "__main__":
    import asyncio
    
    print("🛠️ Инициализация базы данных...")
    asyncio.run(create_tables())
    print("✨ Таблицы успешно созданы!")