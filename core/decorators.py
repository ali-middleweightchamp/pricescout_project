import time
from functools import wraps

# Пишем Декораторы
def time_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️ Время выполнения функции '{func.__name__}': {end_time - start_time:.2f} секунд/ы")
        return result
    return wrapper

def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        retries = 3
        delay = 1
        for attempt in range(1, retries + 1):
            try:
                return func(*args, **kwargs)  
            except Exception as e:
                print(f"⚠️ Ошибка в функции {func.__name__} (Попытка {attempt} из {retries}): {e}")

                if attempt == retries:
                    raise Exception(f"❌ Функция {func.__name__} полностью провалилась после {retries} попыток.")
                
                time.sleep(delay)
    return wrapper


if __name__ == "__main__":
    print("🚀 Тестируем наши декораторы:\n")

    #logger декоратор
    @time_logger
    def sample_function():
        time.sleep(2)
        print("Функция выполнена!")

    sample_function()


    #retry декоратор
    @retry
    def sample_function_with_error():
        print("📡 Пытаемся достучаться до сервера маркетплейса...")
        raise ConnectionError("Код 503: Сервер Uzum перегружен и не отвечает")
    try:
        sample_function_with_error()
    except Exception as e:
        print(f"\n✅ Тест завершен! Декоратор отработал штатно и выбросил финальное исключение:\n{e}")

              

