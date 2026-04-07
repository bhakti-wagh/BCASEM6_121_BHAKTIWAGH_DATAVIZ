import pandas as pd

df = pd.read_csv('iris.csv')
print("Full Dataset Shape:", df.shape)

sample_df = df.sample(n=10, random_state=42)
print("\nSample of 10 rows:")
print(sample_df)

print("\nMaximum values of numeric attributes:")
print(df.select_dtypes(include='number').max())

print("\nMinimum values of numeric attributes:")
print(df.select_dtypes(include='number').min())