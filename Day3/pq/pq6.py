# Write a CSV containing only students scoring above 75.

import csv

def write_above_75(input_file, output_file):
    lst=[]
    with open(input_file,"r") as r:
        reader=csv.DictReader(r)
        for row in reader:
            if int(row["marks"]) > 75:
                lst.append(row)
                return f"CSV FILE IS {output_file} and the students scoring above 75 are {lst}"
print(write_above_75("students.csv","above_75.csv"))

            