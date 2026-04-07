import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Case Study Iris Dataset/iris.csv')
species_count = df['species'].value_counts()

plt.bar(species_count.index, species_count.values,
        color=['blue','orange','green'])
plt.title('Frequency of Iris Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()