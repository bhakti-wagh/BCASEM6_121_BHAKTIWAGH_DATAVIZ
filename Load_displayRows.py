import pandas as pd

df = pd.read_csv('heights_weights.csv')

print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))

print("\nRandom 20 rows:")
print(df.sample(n=20, random_state=1))