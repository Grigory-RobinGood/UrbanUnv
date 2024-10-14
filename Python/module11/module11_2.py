def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, к которому принадлежит объект
    module = obj.__module__

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info


# Пример использования
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2


# Создаем объект класса MyClass
my_object = MyClass(10)

# Проводим интроспекцию объекта
number_info = introspection_info(my_object)
print(number_info)
