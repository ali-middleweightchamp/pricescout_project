import json

def get_flat_categories(data: dict) -> list:
    result = []
    if not data["subcategories"]:
        result.append(data["name"])
    else:
        for subcategory in data["subcategories"]:
            sub_result = get_flat_categories(subcategory)
            result.extend(sub_result)
    return result


if __name__ == "__main__":
    print("🚀 Тестируем рекурсивный обход категорий:\n")

    # Наши тестовые папки-матрёшки
    mock_categories = {
        "name": "Электроника",
        "subcategories": [
            {
                "name": "Смартфоны",
                "subcategories": [
                    {"name": "Apple", "subcategories": []},
                    {"name": "Samsung", "subcategories": []}
                ]
            },
            {
                "name": "Ноутбуки",
                "subcategories": []
            }
        ]
    }
    
    # Запускаем нашу рекурсию
    flat_list = get_flat_categories(mock_categories)
    
    print("🎯 Финальный плоский список для парсера:")
    print(flat_list)