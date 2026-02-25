string = input("Enter main string: ")
substring = input("Enter substring: ")

count = 0
sub_len = len(substring)

for i in range(len(string) - sub_len + 1):
    if string[i:i+sub_len] == substring:
        count += 1

print(count)