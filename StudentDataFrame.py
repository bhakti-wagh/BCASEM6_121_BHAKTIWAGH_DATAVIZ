import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Graduation_Percentage': [85.5, 78.3, 92.1, 88.0, 74.6],
    'Age': [22, 23, 21, 24, 22]
}

df = pd.DataFrame(data)
print(df)

print("\nAverage Age:", df['Age'].mean())
print("Average Graduation Percentage:", df['Graduation_Percentage'].mean())

print("\nBasic Statistics:")
print(df.describe())