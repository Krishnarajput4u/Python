import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 5, 6, np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replace missing values with 0 (or mean, etc.)
df_filled = df.fillna(0)

print("\nAfter replacing missing values:")
print(df_filled)