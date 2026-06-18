import aiohttp
import asyncio
from core.decorators import retry


@retry
async def fetch_raw_data(category_endpoint: str) -> dict:
    url = f"https://jsonplaceholder.typicode.com/{category_endpoint}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return {
                    "status": response.status,
                    "data": await response.json()
                }
            else:
                return {
                    "status": response.status,
                    "error": "Не удалось скачать данные"
                }

            
if __name__ == "__main__":
    result = asyncio.run(fetch_raw_data("posts/1"))
    
    print("Весь результат:", result)
    print("Статус ответа:", result["status"]) 
    print("Данные внутри:", result.get("data"))
