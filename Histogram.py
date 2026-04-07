import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

plt.hist(df['Marks'], bins=5, color='purple', edgecolor='black')
plt.title('Marks Distribution - Histogram')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()