# Build a Python utility that:
# 1. Reads student data from CSV.
# 2. Converts marks into integers.
# 3. Handles invalid marks using try/except.
# 4. Removes invalid records.
# 5. Writes valid records into cleaned.csv.
# 6. Prints how many records were cleaned.

import csv

def clean_student_data(input_file,output_file):
    cleaned_rec=[]
    inval=0
    with open(input_file,"r") as r:
        reader=csv.DictReader(r)
        for row in reader:
            if (0 <= int(row["marks"]) <= 100):
                cleaned_rec.append(row)
            else:
                inval +=1
    with open(output_file,"w",newline="") as f:
        writer =csv.DictWriter(f,fieldnames=["name","age","marks"])
        writer.writeheader()
        writer.writerows(cleaned_rec)
        print(f"Number of cleaned records :{len(cleaned_rec)}")
    print(f"Number of invalid records cleaned: {inval}")
clean_student_data("students.csv","cleaned.csv")