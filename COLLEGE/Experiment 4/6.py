sentence = input("Enter a sentence: ")
words = sentence.split()

unique_words = set(words)

print("Number of unique words:", len(unique_words))