string1="hello"
string2="world"
string3="""This is a multi-line string."""

print(string1)
print(string2)
print(string3)

#Escape characters
string4="This is a string with a newline character.\nThis is the second line."
print(string4)
string5="This is a string with a tab character.\tThis is after the tab."
print(string5)
#Backslash
string6="Hello\\ world"
print(string6)
#single Quote
string7='It\'s a nice day.'
print(string7)
#Double Quote
string8="She said, \"Hello!\""
print(string8)
#carriage return
string9="Hello\rWorld"
print(string9)
#backspace
string10="Hello\bWorld"
print(string10)
#raw string
print(r"This is a raw string with a newline character.\nThis will not be a new line.")

#string Indexing and slicing
string="Hello, World!"

print(string[0])  # H
print(string[7])  # W
print(string[-1]) # !

string="CODE PROGRAMMING"

print(string[0:6])
print(string[7:18])

#omitting start index
print(string[:6])  # CODE P
#omitting end index
print(string[7:])  # PROGRAMMING
#Omitting both start and end index
print(string[:])   # CODE PROGRAMMING
#Negative indexing
print(string[-11:-1])  # ODE PROGRAMMIN
#Using step in slicing
print(string[0:18:2])  # CDPRGAMIG

#reverse string
print(string[::-1])  # GNIMMARGORP EDOC

#string methods
# upper case
string_upper = string.upper()
print(string_upper)
# lower case
string_lower = string.lower()
print(string_lower)
#capitalize
string_capitalized = string.capitalize()
print(string_capitalized)
#title case
string_title = string.title()
print(string_title)
#swapcase
string_swapcase = string.swapcase()
print(string_swapcase)
#casefold
string_casefold = string.casefold()
print(string_casefold)

#ß is converted to ss in casefold
string_with_ss = "Straße"
string_casefolded = string_with_ss.casefold()
print(string_casefolded)  # straße
#Why this happens? The casefold() method is designed to be more aggressive than lower() when it comes to converting characters to lowercase. It is intended for use in case-insensitive comparisons, and it handles certain characters that have special case mappings, such as the German letter "ß". In this case, "ß" is converted to "ss" because that is the standard way to represent it in lowercase form.

#finding substring
index = string.find("PROG")
print(index)  # 7
#rfind
index = string.rfind("PROG")
print(index)  # 7
#index
string ="Hello World"
print(string.index("World"))  # 6
#rindex
print(string.rindex("o"))  # 7
#count
count = string.count("o")
#startswith
print(string.startswith("Hello"))  # True
#endswith
print(string.endswith("World"))  # True

#isaplha
string_alpha = "HelloWorld"
print(string_alpha.isalpha())  # True
#isdigit
string_digit = "12345"
print(string_digit.isdigit())  # True
#isalnum
string_alnum = "Hello123"
print(string_alnum.isalnum())  # True
#isspace
string_space = "   "
print(string_space.isspace())  # True
#islower
string_lowercase = "hello"
print(string_lowercase.islower())  # True
#isupper
string_uppercase = "HELLO"
print(string_uppercase.isupper())  # True
#istitle
string_titlecase = "Hello World"
print(string_titlecase.istitle())  # True
# isdecimal
string_decimal = "12345"
print(string_decimal.isdecimal())  # True
#isnumeric
string_numeric = "12345"
print(string_numeric.isnumeric())  # True
#isidentifier
string_identifier = "variable_name"
print(string_identifier.isidentifier())  # True
#isprintable
string_printable = "Hello\nWorld"
print(string_printable.isprintable())  # False
#strip
string_with_spaces = "   Hello World   "
print(string_with_spaces.strip())  # "Hello World"
#replace
string_replace = "Hello World"
print(string_replace.replace("World", "Python"))  # "Hello Python"
#split
string_split = "Hello, World, Python"
print(string_split.split(", "))  # ['Hello', 'World', 'Python']
#rsplit
string_rsplit = "Hello, World, Python"
print(string_rsplit.rsplit(", ", 1))  # ['Hello, World', 'Python']
#splitlines
string_splitlines = "Hello\nWorld\nPython"
print(string_splitlines.splitlines())  # ['Hello', 'World', 'Python']
#join
string_join = ["Hello", "World", "Python"]
print(", ".join(string_join))  # "Hello, World, Python"

#partition
string_partition = "Hello World Python"
print(string_partition.partition("World"))  # ('Hello ', 'World', ' Python')
#rpartition
string_rpartition = "Hello World Python"
print(string_rpartition.rpartition("World"))  # ('Hello ', 'World', ' Python')
#center
string_center = "Hello"
print(string_center.center(10, "*"))  # "**Hello***"
#ljust
string_ljust = "Hello"
print(string_ljust.ljust(10, "*"))  # "Hello*****"
#rjust
string_rjust = "Hello"
print(string_rjust.rjust(10, "*"))  # "*****Hello"

items = ["Apple", "Banana", "Orange"]
prices = [1.20, 0.80, 1.50]

for item, price in zip(items, prices):
    print(item.ljust(10) + str(price).rjust(10))

# Output:
# Apple          1.2
# Banana         0.8
# Orange         1.5

#zfill
string_zfill = "42"
print(string_zfill.zfill(5))  # "00042"
print("-42".zfill(5))  # "-0042"
print("+42".zfill(5))  # "+0042"
#expandtabs
string_expandtabs = "Hello\tWorld"
print(string_expandtabs.expandtabs(4))  # "Hello   World"
#encode
string = "Hello"

# Default encoding (UTF-8)
encoded = string.encode()
print(encoded)  # b'Hello'
print(type(encoded))  # <class 'bytes'>

# Specific encoding
encoded_ascii = string.encode('ascii')
print(encoded_ascii)  # b'Hello'
print(type(encoded_ascii))  # <class 'bytes'>
#decode
bytes_obj = b'Hello'

decoded = bytes_obj.decode()
print(decoded)  # Hello
print(type(decoded))  # <class 'str'>

#concatination
string1 = "Hello"
string2 = "World"
concatenated = string1 + " " + string2
print(concatenated)  # "Hello World"
#Using+=operator
string1 = "Hello"
string1 += " World"
print(string1)  # "Hello World"

#Multiple concatenation
string1 = "Hello"
string2 = "World"
string3 = "Python"
concatenated = string1 + " " + string2 + " " + string3
print(concatenated)  # "Hello World Python"

#repeating strings
string = "Hello"

repeated = string * 3
print(repeated)  # "HelloHelloHello"
#Membership testing
string = "Hello World"

print("Hello" in string)  # True
print("Python" not in string)  # True

#comparison

string1 = "Hello"
string2 = "World"

print(string1 == string2)  # False
print(string1 != string2)  # True
print(string1 < string2)   # True (because "H" comes before "W")
print(string1 > string2)   # False

#Iteration
string = "Hello"
for char in string:
    print(char,end=" ")  # H e l l o
print()  # for new line

#with index
string = "Hello"
for index, char in enumerate(string):
    print(f"Index: {index}, Character: {char}")
# Output:
# Index: 0, Character: H
# Index: 1, Character: e

# 5. STRING FORMATTING
# CODE
name = "John"
age = 25

# String
print("My name is %s" % name)  # My name is John

# Integer
print("I am %d years old" % age)  # I am 25 years old

# Float
pi = 3.14159
print("Pi = %.2f" % pi)  # Pi = 3.14

# Multiple values
print("My name is %s and I am %d years old" % (name, age))
# My name is John and I am 25 years old

#FORMAT METHOD
name = "John"
age = 25

# Basic
print("My name is {}".format(name))
# My name is John

# Multiple arguments
print("My name is {} and I am {} years old".format(name, age))
# My name is John and I am 25 years old

# Positional arguments
print("I am {1} years old and my name is {0}".format(name, age))
# I am 25 years old and my name is John

# Named arguments
print("My name is {n} and I am {a} years old".format(n=name, a=age))
# My name is John and I am 25 years old

# Formatting numbers
pi = 3.14159
print("Pi = {:.2f}".format(pi))  # Pi = 3.14

# Alignment
print("{:>10}".format("Right"))   # "     Right"
print("{:<10}".format("Left"))    # "Left      "
print("{:^10}".format("Center"))  # "  Center  "

#F-STRINGS 
name = "John"
age = 25

# Basic
print(f"My name is {name}")
# My name is John
# Multiple variables
print(f"My name is {name} and I am {age} years old")
# My name is John and I am 25 years old

# Expressions
print(f"Next year I will be {age + 1} years old")
# Next year I will be 26 years old

# Formatting
pi = 3.14159
print(f"Pi = {pi:.2f}")  # Pi = 3.14

# Alignment
print(f"{'Right':>10}")   # "     Right"
print(f"{'Left':<10}")    # "Left      "
print(f"{'Center':^10}")  # "  Center  "

# Method calls
text = "hello"
print(f"{text.upper()}")  # HELLO

# Dictionary access
person = {"name": "John", "age": 25}
print(f"Name: {person['name']}, Age: {person['age']}")
# Name: John, Age: 25

#len
string = "Hello, World!"
print(len(string))  # 13

#ord
char = 'A'
print(ord(char))  # 65
#chr
code_point = 65
print(chr(code_point))  # A
#max
string = "Hello, World!"
print(max(string))  # r
#min
string = "Hello"
print(min(string))  # H
#sorted
string = "CODE"
print(sorted(string))  # ['h', 'n', 'o', 'p', 't', 'y']

# Join back
print("".join(sorted(string)))  # hnopty

# Reverse sort
print("".join(sorted(string, reverse=True)))  # ytnoph

#reversed
string = "Hello"
print(list(reversed(string)))  # ['o', 'l', 'l', 'e', 'H']

# Join back
print("".join(reversed(string)))  # olleH
