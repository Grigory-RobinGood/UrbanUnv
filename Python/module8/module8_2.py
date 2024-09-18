def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number  # Попытка сложить число
        except TypeError:
            incorrect_data += 1  # Увеличиваем счетчик некорректных данных

    return result, incorrect_data  # Возвращаем кортеж


def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError

        total_sum, incorrect_data = personal_sum(numbers)  # Получаем сумму и количество некорректных данных
        count = len(numbers) - incorrect_data  # Количество корректных данных

        if count == 0:  # Обработка деления на 0
            return 0

        return total_sum / count  # Возвращаем среднее арифметическое

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Примеры использования
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка, некорректный тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
