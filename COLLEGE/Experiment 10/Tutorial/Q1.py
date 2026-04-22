import numpy as np

# Create arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Datatype
a_float = np.array([1, 2, 3], dtype=float)

# Array creation
zeros = np.zeros((2,2))
ones = np.ones((2,2))
arange = np.arange(1,10)
linspace = np.linspace(0,1,5)

# Attributes
matrix = np.array([[1,2],[3,4]])
print("Shape:", matrix.shape)
print("Size:", matrix.size)
print("Datatype:", matrix.dtype)

# Operations
print("Addition:", a + b)
print("Multiplication:", a * b)

# Broadcasting
print("Broadcasting:", a + 2)

# Functions
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Std:", np.std(a))
print("Dot Product:", np.dot(a, b))

# Reshape
reshaped = np.arange(6).reshape(2,3)
print("Reshaped:\n", reshaped)

# Random
rand = np.random.rand(2,2)

# Sorting & Searching
arr = np.array([3,1,2])
print("Sorted:", np.sort(arr))
print("Index of 2:", np.where(arr == 2))

# String
print(np.char.upper(['hello']))