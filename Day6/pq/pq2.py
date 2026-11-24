# Find missing values in a dataset and fill numerical columns using their median.
import pandas as pd
import numpy as np

data = {
    "Name": ["Adarsh", "Rishav", "Sahil", "Surya", "Rohit"],
    "Age": [20, 21, np.nan, 20, np.nan],
    "Marks": [85, np.nan, 90, 78, 88],
    "StudyHours": [3, 5, np.nan, 2, 4]
}

df = pd.DataFrame(data)

# 1. Find missing values
print("Missing values:")
print(df.isnull().sum())

# 2. Fill numerical columns using median
num_cols = df.select_dtypes(include="number").columns

df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# 3. Display cleaned dataset
print("\nCleaned Dataset:")
print(df)