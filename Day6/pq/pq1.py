# Load a CSV containing student records and display the top 5 students by marks.
import pandas as pd

data = {
    "Name": ["Adarsh Raj", "Rishav Raj", "Sahil Raj", "Surya Pratap","Rohit Kumar"],
    
    "Marks": [85, 90, 90, 78, 88],
}
df = pd.DataFrame(data)

print(df.head(5))

#            Name  Marks
# 0    Adarsh Raj     85
# 1    Rishav Raj     90
# 2     Sahil Raj     90
# 3  Surya Pratap     78
# 4   Rohit Kumar     88