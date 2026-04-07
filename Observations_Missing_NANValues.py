import pandas as pd

df = pd.read_csv('heights_weights.csv')

print("Number of observations:", len(df))
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nNaN values per column:")
print(df.isna().sum())