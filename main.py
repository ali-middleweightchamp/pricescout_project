import asyncio
from core.base_parser import DummyParser
from modules.processing import extract_products
from database.models import create_tables, save_product

async def main():
    print("Запуск мониторинга цен...")

    await create_tables()

    parser = DummyParser()
    print("\n⏳ Скачиваем сырые данные...")

    raw_data = await parser.fetch_raw_data()

    print("🧹 Запуск конвейера очистки и сохранения...")
    for product in extract_products(raw_data):
        await save_product(product)
        print(f"💾 [БАЗА] Успешно сохранен: {product.name} ({product.price} сум)")
    print("\n✨ Работа успешно завершена. Все данные на складе!")


if __name__ == "__main__":
    asyncio.run(main())
