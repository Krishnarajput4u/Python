def remove_duplicates(string):
    result = ""
    seen = set()

    for char in string:
        if char not in seen:
            result += char
            seen.add(char)

    return result


print(remove_duplicates("programming"))