import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Case Study Iris Dataset/iris.csv')
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
species_count = df['species'].unique()

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

for ax, feature in zip(axes.flatten(), features):
    data_to_plot = [df[df['species'] == sp][feature].values for sp in species_count]
    ax.boxplot(data_to_plot, labels=species_count)
    ax.set_title(f'Box Plot of {feature}')
    ax.set_xlabel('Species')
    ax.set_ylabel(feature)
    ax.tick_params(axis='x', rotation=15)

plt.tight_layout()
plt.show()