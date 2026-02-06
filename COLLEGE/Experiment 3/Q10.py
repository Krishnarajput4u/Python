n = 5

# First row: 123454321
for i in range(1, n + 1):
    print(i, end='')
for i in range(n - 1, 0, -1):
    print(i, end='')
print()

# Remaining rows
for row in range(1, n):
    # Left numbers
    for i in range(1, n - row + 1):
        print(i, end='')
    
    
    # Stars with spaces between
    for i in range(row):
        print('*', end='')
        if i < row - 1:
            print(' ', end='')
    
    # Right numbers
    for i in range(n - row, 0, -1):
        print(i, end='')
    print()