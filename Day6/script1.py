import numpy as np
import pandas as pd

data = {
    "Name": ["Adarsh Raj", "Rishav Raj", "Sahil Raj", "Surya Pratap","Rohit Kumar"],
    "Age": [21, 22, 20, 22, np.nan],
    "Marks": [85, 90, np.nan, 78, 88],
    "City": ["Delhi", "Jaipur", "Delhi", "Mumbai", "Jaipur"]
}

df=pd.DataFrame(data)
print(df)

df1=pd.read_csv("students.csv")

print(df)
print("------------------------------------------------------")
df.to_csv("cleaned_students.csv", index=False)
print("------------------------------------------------------")
print(df1.describe())
print("------------------------------------------------------")
print(df.info())
print("------------------------------------------------------")
print(df.columns)
print("------------------------------------------------------")
print(df.shape)
print("------------------------------------------------------")
print(df.isnull())

# Remove rows where all values are missing
df.dropna(how="all")

# Remove columns containing missing values
df.dropna(axis=1)

# Remove rows having missing values in specific columns
df.dropna(subset=["Age"])