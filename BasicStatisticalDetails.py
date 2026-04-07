import pandas as pd

df = pd.read_csv('heights_weights.csv')

print("Basic Statistical Details:")
print(df.describe())