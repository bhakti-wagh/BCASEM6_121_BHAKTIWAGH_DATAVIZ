import pandas as pd

df = pd.read_csv('heights_weights.csv')

# Convert inches to meters and pounds to kg first
df['Height_m'] = df['Height(Inches)'] * 0.0254
df['Weight_kg'] = df['Weight(Pounds)'] * 0.453592

df['BMI'] = df['Weight_kg'] / (df['Height_m'] ** 2)

print(df[['Height(Inches)', 'Weight(Pounds)', 'BMI']].head(10))