import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.random.randint(1, 100, 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0,0].plot(data, color='blue')
axes[0,0].set_title('Line Chart')
axes[0,0].set_xlabel('Index')
axes[0,0].set_ylabel('Value')

axes[0,1].scatter(range(50), data, color='red')
axes[0,1].set_title('Scatter Plot')
axes[0,1].set_xlabel('Index')
axes[0,1].set_ylabel('Value')

axes[1,0].hist(data, bins=10, color='green', edgecolor='black')
axes[1,0].set_title('Histogram')
axes[1,0].set_xlabel('Value')
axes[1,0].set_ylabel('Frequency')

axes[1,1].boxplot(data)
axes[1,1].set_title('Box Plot')
axes[1,1].set_ylabel('Value')

plt.tight_layout()
plt.show()