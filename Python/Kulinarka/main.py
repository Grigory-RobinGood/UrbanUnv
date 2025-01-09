import os


def read_recipes(directory):
    recipes = {}
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            try:
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    dish_name = lines[0].strip()
                    ingredients = [line.strip() for line in lines[1:] if line.strip()]
                    instructions = []
                    for line in lines:
                        if line.strip() == '':
                            break
                        instructions.append(line.strip())
                    recipes[dish_name] = {
                        'ingredients': ingredients,
                        'instructions': instructions
                    }
            except FileNotFoundError:
                print(f"Файл {filename} не найден.")
    return recipes


def write_summary(recipes, summary_file='summary.txt'):
    with open(summary_file, 'w', encoding='utf-8') as file:
        for dish, details in recipes.items():
            file.write(f"{dish}\n")
            file.write("Ингредиенты:\n")
            for ingredient in details['ingredients']:
                file.write(f"- {ingredient}\n")
            file.write("\n")


def create_shopping_list(recipes, shopping_list_file='shopping_list.txt'):
    all_ingredients = set()  # Используем множество для уникальности
    for details in recipes.values():
        all_ingredients.update(details['ingredients'])
    with open(shopping_list_file, 'w', encoding='utf-8') as file:
        for ingredient in sorted(all_ingredients):  # Сортируем перед записью
            file.write(f"{ingredient}\n")


def filter_recipes_by_ingredient(recipes, ingredient):
    filtered = {}
    for dish, details in recipes.items():
        if ingredient in details['ingredients']:
            filtered[dish] = details
    return filtered


def show_instructions(recipes, dish_name):
    if dish_name in recipes:
        print(f"Инструкции по приготовлению {dish_name}:")
        for instruction in recipes[dish_name]['instructions']:
            print(instruction)
    else:
        print(f"Рецепт для {dish_name} не найден.")


def update_recipe(directory, dish_name, ingredients, instructions):
    filename = os.path.join(directory, f"{dish_name}.txt")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"{dish_name}\n")
        for ingredient in ingredients:
            file.write(f"{ingredient}\n")
        file.write("\n")
        for instruction in instructions:
            file.write(f"{instruction}\n")


# Пример использования
directory = 'recipes'  # Укажите путь к директории с рецептами
recipes = read_recipes(directory)

# Создание сводного файла
write_summary(recipes)

# Создание файла со списком покупок
create_shopping_list(recipes)

# Ввод пользователем названия ингредиента для фильтрации
ingredient_to_filter = input("Введите ингредиент для фильтрации рецептов: ")
filtered_recipes = filter_recipes_by_ingredient(recipes, ingredient_to_filter)
if filtered_recipes:
    print(f"Рецепты с ингредиентом '{ingredient_to_filter}': {filtered_recipes.keys()}")
else:
    print(f"Нет рецептов с ингредиентом '{ingredient_to_filter}'.")

# Ввод пользователем названия рецепта для отображения инструкций
dish_to_show = input("Введите название блюда для отображения инструкций: ")
show_instructions(recipes, dish_to_show)

# Обновление рецепта
#update_recipe(directory, 'Новый Пирог', ['мука', 'яйца', 'сахар'], ['Смешать все ингредиенты', 'Выпекать 30 минут.'])
