import matplotlib.pyplot as plt

x = [1,2,3]
y = [10,20,30]

# Line plot
plt.plot(x, y, marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")
plt.grid()
plt.show()

# Bar chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# Histogram
plt.hist(y)
plt.title("Histogram")
plt.show()

# Scatter plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Pie chart
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# Subplots
plt.subplot(1,2,1)
plt.plot(x,y)

plt.subplot(1,2,2)
plt.bar(x,y)

plt.show()