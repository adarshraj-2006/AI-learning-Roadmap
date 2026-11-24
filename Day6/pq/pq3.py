# Filter employees whose salary is above ₹30,000 and age is below 30.
import numpy as np
import pandas as pd
data = {
    "Name": ["Adarsh", "Rishav", "Sahil", "Surya", "Rohit"],
    "Age": [20, 21, np.nan, 20, np.nan],
    "Salary": [85000, np.nan, 23000, 78000, 89000],
    "StudyHours": [3, 5, np.nan, 2, 4]
}
df=pd.DataFrame(data)
result=df[(df["Salary"] > 30000) & (df["Age"] > 18)]
print(result)

#      Name   Age   Salary  StudyHours
# 0  Adarsh  20.0  85000.0         3.0
# 3   Surya  20.0  78000.0         2.0