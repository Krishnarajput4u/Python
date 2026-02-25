def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - start + shift) % 26 + start)
            result += shifted
        else:
            result += char

    return result


text = "Hello World"
encrypted = caesar_cipher(text, 3)
print("Encrypted:", encrypted)

decrypted = caesar_cipher(encrypted, -3)
print("Decrypted:", decrypted)