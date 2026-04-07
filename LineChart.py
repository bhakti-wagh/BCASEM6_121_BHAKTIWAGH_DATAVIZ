import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

plt.plot(df['Subject'], df['Marks'], color='green', marker='o', linestyle='-')
plt.title('Subject vs Marks - Line Chart')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.grid(True)
plt.show()