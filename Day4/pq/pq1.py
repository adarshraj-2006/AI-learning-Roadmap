# Create a dataset containing marks of 4 students in 3 subjects. 
# Calculate each student's average, identify the highest scorer, and 
# extract marks of a particular subject.

import numpy as np

marks = np.array([
    [80, 90, 85],
    [70, 75, 80],
    [95, 92, 98],
    [60, 65, 70]
])

student_avg = np.mean(marks, axis=1)

print("Student averages:", student_avg)
print("Highest average:", np.max(student_avg))
print("Highest scorer index:", np.argmax(student_avg))
print("Math marks:", marks[:, 0])
