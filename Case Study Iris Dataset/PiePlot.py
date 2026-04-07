import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Case Study Iris Dataset/iris.csv')
species_count = df['species'].value_counts()

plt.pie(species_count.values, labels=species_count.index,
        autopct='%1.1f%%', colors=['blue','orange','green'])
plt.title('Iris Species Distribution - Pie Chart')
plt.show()