def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()     # приводим все символы первого слова к нижнему регистру
    same_words = []                         # создаем пустой список

    for word in other_words:
        word_lower = word.lower()           # приводим второе слово к нижнему регистру

        if root_word_lower in word_lower or word_lower in root_word_lower: # проверяем совпадения
            same_words.append(word)         # добавляем в список совпадения

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
