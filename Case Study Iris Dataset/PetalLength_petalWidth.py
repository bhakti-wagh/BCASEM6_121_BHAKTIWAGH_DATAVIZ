import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')
species = df['class'].unique()
colors = ['blue', 'orange', 'green']

for sp, col in zip(species, colors):
    subset = df[df['class'] == sp]
    plt.scatter(subset['petal_length'], subset['petal_width'],
                label=sp, color=col, alpha=0.7)

plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend()
plt.grid(True)
plt.show()