import pandas as pd

df = pd.read_csv('iris.csv')

print("Number of records for each class:")
print(df['class'].value_counts())

print("\nColumn-wise Mean:")
print(df.select_dtypes(include='number').mean())

print("\nColumn-wise Median:")
print(df.select_dtypes(include='number').median())