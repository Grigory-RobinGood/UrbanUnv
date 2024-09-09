import os
import time


def file_info(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            # Формируем полный путь к файлу
            file_path = os.path.join(dirpath, filename)

            # Получаем время последнего изменения
            last_modified_time = os.path.getmtime(file_path)
            last_modified_time_str = time.ctime(last_modified_time)  # Преобразуем в читаемый формат

            # Получаем размер файла
            file_size = os.path.getsize(file_path)

            # Получаем родительскую директорию
            parent_directory = os.path.dirname(file_path)

            # Выводим информацию о файле
            print(f"Файл: {file_path}")
            print(f"  Последнее изменение: {last_modified_time_str}")
            print(f"  Размер: {file_size} байт")
            print(f"  Родительская директория: {parent_directory}")
            print("-" * 40)


# Пример использования
directory = r'D:\UrbanUnv\Python\module7'
file_info(directory)
