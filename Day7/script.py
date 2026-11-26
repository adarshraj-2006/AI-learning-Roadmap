import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Name": ["Aman", "Rahul", "Priya", "Riya", "Karan",
             "Neha", "Sahil", "Anjali", "Vikas", "Rohit"],
    "Marks": [45, 67, 82, 90, 56, 72, 88, 95, 63, 78],
    "StudyHours": [2, 3, 5, 7, 2, 4, 6, 8, 3, 5],
    "Age": [18, 19, 18, 20, 19, 18, 20, 19, 18, 20]
}
df=pd.DataFrame(data)
print(df)

#using histogram
plt.hist(df["Marks"],bins=5,edgecolor="black")
plt.title("Distribution of Student marks ")
plt.xlabel("Marks")   #x-axis
plt.ylabel("No of students")
# plt.show()

#using scatter plot
plt.scatter(df["StudyHours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks of Students")
# plt.show()

#Bargraph
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].hist(df["Marks"], bins=5, edgecolor="black")
axes[0].set_title("Marks Distribution")

axes[1].scatter(df["StudyHours"], df["Marks"])
axes[1].set_title("Study Hours vs Marks")
axes[1].set_xlabel("Study Hours")
axes[1].set_ylabel("Marks")

axes[2].bar(df["Name"], df["Marks"])
axes[2].set_title("Student Marks")
axes[2].tick_params(axis="x", rotation=90)

plt.tight_layout()
plt.show()