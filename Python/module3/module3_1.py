calls = 0


def count_calls():  # Создаем счетчик вызовов
    global calls
    calls += 1


def string_info(string):   # Увеличиваем счетчик вызовов
    count_calls()
    length = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    return length, upper_string, lower_string


def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_to_search_lower = [item.lower() for item in list_to_search]
    return string_lower in list_to_search_lower


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)
