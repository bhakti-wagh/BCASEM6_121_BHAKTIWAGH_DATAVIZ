import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Case Study Iris Dataset/iris.csv')
species_count = df['species'].unique()

colors = ['blue', 'orange', 'green']

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for sp, col in zip(species_count, colors):
    subset = df[df['species'] == sp]
    axes[0].scatter(subset['sepal_length'], subset['sepal_width'],
                    label=sp, color=col, alpha=0.7)
    axes[1].scatter(subset['petal_length'], subset['petal_width'],
                    label=sp, color=col, alpha=0.7)

axes[0].set_title('Sepal Length vs Sepal Width')
axes[0].set_xlabel('Sepal Length')
axes[0].set_ylabel('Sepal Width')
axes[0].legend()

axes[1].set_title('Petal Length vs Petal Width')
axes[1].set_xlabel('Petal Length')
axes[1].set_ylabel('Petal Width')
axes[1].legend()

plt.tight_layout()
plt.show()