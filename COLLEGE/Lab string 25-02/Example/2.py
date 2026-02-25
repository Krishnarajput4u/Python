def is_palindrome(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()
    return string == string[::-1]


print(is_palindrome("racecar"))  
print(is_palindrome("A man a plan a canal Panama"))