marks = [45, 78, 32, 90, 67, 88, 25, 76, 55, 95]
print("Marks:", marks)

filtered_marks=[x for x in marks if x > 40]
print("Filtered marks:", filtered_marks)

def avg_marks(marks):
    return sum(marks) / len(marks)
print("Average marks:", avg_marks(filtered_marks))

def get_highmarks(marks):
    m=marks[0]
    [m:=x for x in marks if x > m]
    print(m)
print(get_highmarks(marks))

def get_lowermarks(marks):
    m=marks[0]
    [m:= x for x in marks if x < m]
    print(m)
print(get_lowermarks(marks))

def count_stud(marks):
    avg=avg_marks(marks)
    count=0
    [count := count + 1 for x in marks if x > avg]
    print(count)
print(count_stud(marks))
