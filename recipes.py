cook_book = {
  "Омлет": [
    {"ingredient_name": "Яйцо", "quantity": 2, "measure": "шт."},
    {"ingredient_name": "Молоко", "quantity": 100, "measure": "мл"},
    {"ingredient_name": "Помидор", "quantity": 2, "measure": "шт"}
  ],
  "Утка по-пекински": [
    {"ingredient_name": "Утка", "quantity": 1, "measure": "шт"},
    {"ingredient_name": "Вода", "quantity": 2, "measure": "л"},
    {"ingredient_name": "Мед", "quantity": 3, "measure": "ст.л"},
    {"ingredient_name": "Соевый соус", "quantity": 60, "measure": "мл"}
  ],
  "Запеченный картофель": [
    {"ingredient_name": "Картофель", "quantity": 1, "measure": "кг"},
    {"ingredient_name": "Чеснок", "quantity": 3, "measure": "зубч"},
    {"ingredient_name": "Сыр гауда", "quantity": 100, "measure": "г"}
  ]
}

import json

# Функция для загрузки книги рецептов из файла
def load_cook_book(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Загрузка рецептов
cook_book = load_cook_book('cook_book.json')

# Пример использования
for dish, ingredients in cook_book.items():
    print(f'Рецепт: {dish}')
    for ingredient in ingredients:
        print(f"{ingredient['ingredient_name']}: {ingredient['quantity']} {ingredient['measure']}")
    print()  # Пустая строка для разделения рецептов