import pandas as pd

data = {'X':[1,2,3,4,5],
        'Y':[6,7,8,9,10]}

df = pd.DataFrame(data)

print(df)

# Example: X^Y (you can change columns as needed)
power_result = df['X'] ** df['Y']

print("\nElement-wise power (X^Y):")
print(power_result)