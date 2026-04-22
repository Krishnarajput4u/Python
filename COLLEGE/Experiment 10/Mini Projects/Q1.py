import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Aman', 'Riya', 'John', 'Neha'],
    'Maths': [80, 90, 75, 85],
    'Science': [85, 88, 78, 90],
    'English': [78, 92, 80, 86]
}

df = pd.DataFrame(data)

marks = df[['Maths','Science','English']].values

print("Average Marks:", np.mean(marks))
print("Total Marks:", np.sum(marks))

df['Average'] = df[['Maths','Science','English']].mean(axis=1)

plt.bar(df['Name'], df['Average'])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance")
plt.show()