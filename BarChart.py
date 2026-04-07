import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

plt.bar(df['Subject'], df['Marks'], color='orange')
plt.title('Subject vs Marks - Bar Chart')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.show()