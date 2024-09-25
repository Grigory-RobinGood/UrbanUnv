def all_variants(text):
    length = len(text)

    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]


text_input = "abc"
subsequences = all_variants(text_input)


for subsequence in subsequences:
    print(subsequence)
