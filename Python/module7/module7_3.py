class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов в виде кортежа

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Читаем все строки, приводим к нижнему регистру и убираем пунктуацию
                    lines = file.readlines()
                    words = []
                    for line in lines:
                        # Убираем пунктуацию и разбиваем строку на слова
                        line = line.lower()
                        line = ''.join(char for char in line if char.isalnum() or char.isspace())  # Убираем пунктуацию
                        words.extend(line.split())
                    all_words[file_name] = words  # Сохраняем в словарь

            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            if word.lower() in words:
                position = words.index(word.lower()) + 1  # Позиция слова (1-based index)
                result[file_name] = position

        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                result[file_name] = count

        return result


# Пример использования
if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # Позиция слова
    print(finder2.count('teXT'))  # Количество слов