import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Line plot
plt.plot(x, y)
plt.title("Line Plot")
plt.show()

# Bar chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# Scatter plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Pie chart
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()