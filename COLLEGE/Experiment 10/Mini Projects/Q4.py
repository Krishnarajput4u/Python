import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

print(df.head())

df.fillna(0, inplace=True)

plt.scatter(df['X'], df['Y'])
plt.title("CSV Data Plot")
plt.show()