import os

filename = "counter.txt"

# Check if file exists
if os.path.exists(filename):

    file = open(filename, "r")
    count = int(file.read())
    file.close()

else:
    count = 0

# Increase counter
count += 1

file = open(filename, "w")
file.write(str(count))
file.close()

print("Program executed", count, "times.")
