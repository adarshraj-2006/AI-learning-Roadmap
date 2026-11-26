# Part 1 — Data processing (Pandas)
# - [ ] Create a dataset with 15–20 students and 3 subjects.
# - [ ] Convert the dataset into a DataFrame.
# - [ ] Find missing values and handle them.
# - [ ] Calculate total and average marks per student.
# - [ ] Filter students scoring above 75 average marks.
# - [ ] Sort students from highest to lowest average.
# - [ ] Identify the topper and lowest-performing student.

# Part 2 — Numerical analysis (NumPy)
# - [ ] Convert marks into NumPy arrays.
# - [ ] Calculate subject-wise mean.
# - [ ] Find maximum and minimum marks.
# - [ ] Calculate standard deviation.
# - [ ] Compare NumPy results with Pandas results.

# Part 3 — Visualization (Matplotlib)
# - [ ] Bar chart → Compare average marks of students.
# - [ ] Histogram → Show distribution of student marks.
# - [ ] Scatter plot → Maths marks vs Science marks.
# - [ ] Bar chart → Compare average marks across subjects.
# - [ ] Write 5 meaningful observations from your graphs.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# student dataset
dataset={
    "Name":["Adarsh Raj","Naman Kumar","Aman Abhi","Ohm Singh","Sahil Singh","Aditya Raj",
            "Rishav Raj","Surya Pratap","Sanya Sharma"],
    "Science":[70,75,89,80,94,98,91,97,84],
    "Math":[76,87,54,87,87,65,97,67,88],
    "English":[86,54,87,87,67,98,85,86,66]
}
df=pd.DataFrame(dataset)
print(df)