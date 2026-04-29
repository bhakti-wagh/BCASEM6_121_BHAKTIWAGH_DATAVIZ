#generate random array and display using different charts

import numpy as np
import matplotlib.pyplot as plt

# Generate random array of 50 integers
data = np.random.randint(1, 100, 50)

# -----------------------------
# Line Chart
# -----------------------------
plt.plot(data, color='blue', marker='o', linestyle='-')
plt.title("Line Chart of Random Data")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid(True)
plt.show()

# -----------------------------
# Scatter Plot
# -----------------------------
plt.scatter(range(50), data, color='red')
plt.title("Scatter Plot of Random Data")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()

# -----------------------------
# Histogram
# -----------------------------
plt.hist(data, bins=10, color='green')
plt.title("Histogram of Random Data")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# Box Plot
# -----------------------------
plt.boxplot(data)
plt.title("Box Plot of Random Data")
plt.show()
