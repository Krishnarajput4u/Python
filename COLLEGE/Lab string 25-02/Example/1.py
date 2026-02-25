def count_vowels_consonants(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in string:
        if char.isalpha():  # Check only alphabet characters
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


text = "Hello World"
v, c = count_vowels_consonants(text)
print(f"Vowels: {v}, Consonants: {c}")