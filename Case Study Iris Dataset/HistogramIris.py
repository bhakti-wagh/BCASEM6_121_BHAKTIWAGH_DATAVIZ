import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')
species = df['class'].unique()
colors = ['blue', 'orange', 'green']

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for ax, feature in zip(axes.flatten(), features):
    for sp, col in zip(species, colors):
        subset = df[df['class'] == sp]
        ax.hist(subset[feature], alpha=0.6, label=sp, color=col, bins=15)
    ax.set_title(f'Histogram of {feature}')
    ax.set_xlabel(feature)
    ax.set_ylabel('Frequency')
    ax.legend()

plt.tight_layout()
plt.show()