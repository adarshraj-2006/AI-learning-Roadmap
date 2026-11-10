# Read a CSV and calculate the average marks
import csv 
def avg_marks_from_csv(file):
    marks=[]
    with open(file,'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            marks.append(int(row["marks"]))
    return sum(marks) / len(marks) if marks else 0

print(f"The average marks from the CSV file is : {avg_marks_from_csv('students_avg.csv')}")