import pandas as pd

# Series
s = pd.Series([10,20,30])
print(s)

print("Head:\n", s.head())
print("Tail:\n", s.tail())
print("Add 5:\n", s + 5)

# DataFrame
data = {
    'Name': ['A','B'],
    'Marks': [80,90]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Column operations
print("Names:", df['Name'])

df['Grade'] = ['A','A+']
print("After adding column:\n", df)

df.drop('Grade', axis=1, inplace=True)

# Iteration
for i in df['Name']:
    print("Student:", i)

# Binary operations
df1 = df.copy()
print("Addition:\n", df1 + df1)

# Missing data
df_missing = df.copy()
df_missing.loc[1, 'Marks'] = None
print("Fill NA:\n", df_missing.fillna(0))
print("Drop NA:\n", df_missing.dropna())

# Aggregation
print("Sum:", df['Marks'].sum())
print("Mean:", df['Marks'].mean())

# Comparison
print("Marks > 80:\n", df['Marks'] > 80)

# Combine
combined = pd.concat([df, df])
print("Combined:\n", combined)

# CSV
df.to_csv('data.csv', index=False)
df2 = pd.read_csv('data.csv')
print("Read CSV:\n", df2)