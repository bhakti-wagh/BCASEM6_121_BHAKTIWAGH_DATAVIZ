import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.random.randint(1, 100, 50)
data_with_outliers = np.append(data, [200, -50])  # 2 outliers added

plt.boxplot(data_with_outliers)
plt.title('Box Plot with Outliers')
plt.ylabel('Value')
plt.show()