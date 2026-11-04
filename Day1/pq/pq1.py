# 1. Sort Students by Marks
# Also called as Bubble Sort Algorithm
# we can also implement this using merge sort or quick for n logn tc

dict =[('aman',90),('Rishav raj',99),('Adarsh Raj',87),('Sahil Raj',97)]

def sort_by_marks(dict):
    for i in range(len(dict)):
        for j in range(len(dict)-i-1):
            if dict[j][1] < dict[j+1][1]:
                dict[j],dict[j+1]=dict[j+1],dict[j]
    return dict
print(sort_by_marks(dict))

# output : [('Rishav raj', 99), ('Sahil Raj', 97), ('aman', 90), ('Adarsh Raj', 87)]