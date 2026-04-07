import pandas as pd

df = pd.read_csv('heights_weights.csv')

print("Shape:", df.shape)
print("Size:", df.size)
print("\nDatatypes:")
print(df.dtypes)