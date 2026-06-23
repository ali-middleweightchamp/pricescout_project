import aiosqlite
from contextlib import asynccontextmanager

DB_PATH = "database/pricescout.db"

@asynccontextmanager
async def get_db_connection():
    conn = await aiosqlite.connect(DB_PATH)
    try:
        conn.row_factory = aiosqlite.Row
        yield conn
    finally:
        await conn.close()


if __name__ == "__main__":
    import asyncio

    async def test_connection():
        print("🔌 Пробуем подключиться к базе данных...")
        try:
            async with get_db_connection() as conn:
                conn.row_factory = aiosqlite.Row
                async with conn.execute("SELECT sqlite_version();") as cursor:
                    version = await cursor.fetchone()
                    print(f"✅ Успешно! Версия SQLite: {version[0]}")
        except Exception as e:
            print(f"❌ Ошибка подключения: {e}")
    


