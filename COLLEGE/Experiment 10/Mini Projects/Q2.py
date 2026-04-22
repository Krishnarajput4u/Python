import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [200, 250, 300, 280]

df = pd.DataFrame({
    'Month': months,
    'Sales': sales
})

arr = np.array(sales)

print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Mean:", np.mean(arr))

# Line plot
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title("Sales Trend")
plt.grid()
plt.show()

# Pie chart
plt.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%')
plt.show()