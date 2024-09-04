from pprint import pprint


class Product:  #Создаем класс продукты

    def __init__(self, name, weight, category):  #Инициализируем атрибуты класса
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):  #возвращаем содержимое класса
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:  #Создаем класс магазин
    def __init__(self):  #Инициализируем инкапсулированный атрибут
        self.__file_name = 'product.txt'

    def get_products(self):  #Функция чтения файла
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()

        except FileNotFoundError:
            return "Файл не найден"

    def add(self, *products):  #функция добавления товаров в магазин
        existing_products = self.get_products().splitlines()  # Получаем существующие продукты
        existing_names = [line.split(', ')[0] for line in
                          existing_products]  # Извлекаем названия существующих продуктов

        for product in products:
            if product.name in existing_names:
                print(f"Продукт {product.name} уже есть в магазине")  # Сообщение, если продукт уже существует
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')  # Записываем новый продукт в файл


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
