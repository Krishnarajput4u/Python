import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(10, 100, 50)

plt.hist(data)
plt.title("Random Data Distribution")
plt.show()

print("Mean:", np.mean(data))
print("Std:", np.std(data))