def calculate_structure_sum(data):
    total_sum = 0

    for element in data:
        if isinstance(element, (int, float)):  # Если элемент - число
            total_sum += element
        elif isinstance(element, str):  # Если элемент - строка
            total_sum += len(element)
        elif isinstance(element, list):  # Если элемент - список
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов для списка
        elif isinstance(element, tuple):  # Если элемент - кортеж
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов для кортежа
        elif isinstance(element, set):  # Если элемент - множество
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов для множества
        elif isinstance(element, dict):  # Если элемент - словарь
            total_sum += sum(len(key) for key in element.keys())  # Сумма длин ключей
            total_sum += calculate_structure_sum(list(element.values()))  # Сумма по значениям

    return total_sum


data_structure = [
    [1, 2, 3],  # Сумма: 1 + 2 + 3 = 6
    {'a': 4, 'b': 5},  # Сумма: длина 'a' + длина 'b' + 4 + 5 = 1 + 1 + 4 + 5 = 11
    (6, {'cube': 7, 'drum': 8}),  # Сумма: длина 'cube' + длина 'drum' + 6 + 7 + 8 = 4 + 4 + 6 + 7 + 8 = 29
    "Hello",  # Длина строки: 5
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # Сумма: длина 'Urban' + длина 'Urban2' + 2 + 35 = 6 + 8 + 2 + 35 = 51
]

result = calculate_structure_sum(data_structure)
print(result)  # Проверяем результат
