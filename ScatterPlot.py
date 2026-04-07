import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

plt.scatter(df['Marks'], df['Students'], color='blue', marker='o')
plt.title('Marks vs Students - Scatter Plot')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.grid(True)
plt.show()