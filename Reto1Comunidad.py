def is_anagram(word1, word2):
    word1_cleaned = sorted(word1.lower().strip()) #crea una lista ORDENADA con los elementos de la palabra, en minuscula y sin espacios.
    word2_cleaned = sorted(word2.lower().strip()) #sorted(iterable, key=key, reverse=reverse) 

    if (word1 == word2 or len(word1_cleaned) != len(word2_cleaned) or word1_cleaned != word2_cleaned):
        return False
    return True

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
print(f"Is the second word an anagram? {is_anagram(word1, word2)}") 

