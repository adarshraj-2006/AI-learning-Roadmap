
# Python Basic to Medium Notes

## 1. Variables and Data Types
```python
name = "Adarsh"
age = 20
price = 99.5
is_student = True
print(type(name))
```
- int: 10, float: 10.5, str: "Hello", bool: True/False
- Type conversion: `int("10")`, `float("5.5")`, `str(100)`

## 2. Input and Output
```python
name = input("Name: ")
age = int(input("Age: "))
print(f"{name} is {age} years old")
```

## 3. Operators
- Arithmetic: `+ - * / // % **`
- Comparison: `== != > < >= <=`
- Logical: `and or not`
```python
print(10 // 3)  # 3
print(10 % 3)   # 1
```

## 4. Conditions
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```
- Ternary: `result = "Even" if n%2==0 else "Odd"`

## 5. Strings
```python
s = "Python Programming"
print(s[0], s[-1], s[0:6], s[::-1])
print(s.lower(), s.upper(), s.replace("Python","Java"))
print(s.split())
```
- Methods: `strip()`, `split()`, `join()`, `find()`, `count()`
- Strings are immutable.

## 6. Lists
```python
nums = [10, 20, 30, 40]
print(nums[0], nums[-1], nums[1:3])
nums.append(50)
nums.insert(1,15)
nums.remove(20)
nums.pop()
```
- Methods: `append()`, `insert()`, `extend()`, `remove()`, `pop()`, `sort()`, `reverse()`, `clear()`
- Lists are ordered, mutable, and allow duplicates.

## 7. List Comprehension
```python
nums = [1,2,3,4,5]
squares = [x*x for x in nums]
even = [x for x in nums if x%2==0]
```
- Syntax: `[expression for item in iterable if condition]`

## 8. Tuples
```python
t = (10,20,30,40)
print(t[0], t[-1], t.count(10), t.index(30))
name, age = ("Adarsh",20)
```
- Tuples are ordered and immutable.
- Single element tuple: `(10,)`

## 9. Dictionaries
```python
student = {"name":"Adarsh","age":20,"marks":90}
print(student["name"], student.get("age"))
student["city"] = "Jaipur"
student.update({"marks":95})
student.pop("age")
```
- Methods: `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`, `clear()`
```python
for k,v in student.items():
    print(k,v)
```

## 10. Dictionary Comprehension
```python
nums = [1,2,3,4]
squares = {x:x*x for x in nums}
```
- Filter: `{k:v for k,v in d.items() if v>80}`

## 11. Sets
```python
a = {1,2,3}
b = {3,4,5}
print(a|b, a&b, a-b, a^b)
```
- Sets store unique elements.
- Methods: `add()`, `remove()`, `discard()`

## 12. Loops
```python
for i in range(5):
    print(i)
i = 1
while i <= 5:
    print(i)
    i += 1
```
- `range(start,stop,step)`
- `break` terminates loop; `continue` skips iteration.
- Nested loops are loops inside loops.

## 13. Functions
```python
def add(a,b):
    return a+b
print(add(10,20))
```
- Default argument: `def greet(name="User"):`
- `*args` accepts multiple positional arguments.
- `**kwargs` accepts multiple keyword arguments.
```python
def total(*nums):
    return sum(nums)
```

## 14. Lambda, Map, Filter
```python
square = lambda x:x*x
print(square(5))
print(list(map(lambda x:x*x,[1,2,3])))
print(list(filter(lambda x:x%2==0,[1,2,3,4])))
```
- Lambda creates a small anonymous function.
- Map transforms elements; filter selects elements.

## 15. Sorting
```python
nums = [5,2,8,1]
print(sorted(nums))
nums.sort()
```
```python
students = [("Ravi",80),("Neha",95)]
print(sorted(students,key=lambda x:x[1],reverse=True))
```
- `sorted()` returns new list; `sort()` modifies original.

## 16. Useful Functions
- `len()`, `sum()`, `max()`, `min()`, `sorted()`, `range()`
- `enumerate()` gives index and value.
- `zip()` combines multiple iterables.
```python
for i,x in enumerate([10,20,30]): print(i,x)
for a,b in zip([1,2],[3,4]): print(a,b)
```

## 17. Exception Handling
```python
try:
    n = int(input())
    print(10/n)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide")
finally:
    print("Completed")
```
- `try`: risky code; `except`: handles errors; `finally`: always executes.

## 18. File Handling
```python
with open("data.txt","w") as f:
    f.write("Hello Python")
with open("data.txt","r") as f:
    print(f.read())
```
- Modes: `r` read, `w` write, `a` append.

## 19. OOP Basics
```python
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name,self.marks)
s = Student("Adarsh",90)
s.display()
```
- Class is blueprint; object is instance; `self` refers to current object.
- Inheritance allows one class to reuse another class's properties.

## 20. Important Problem-Solving Patterns
```python
# Frequency
freq = {}
for x in [1,2,2,3]:
    freq[x] = freq.get(x,0)+1

# Largest without max()
nums = [10,50,20]
largest = nums[0]
for x in nums:
    if x > largest: largest = x

# Remove duplicates preserving order
result = list(dict.fromkeys([1,2,2,3]))

# Palindrome
s = "madam"
print(s == s[::-1])
```

## Practice
1. Find second-largest number in a list.
2. Count character frequency using dictionary.
3. Filter students scoring above 80.
4. Find common elements between two lists.
5. Sort employees by salary.
6. Find highest and second-highest salary.
7. Group anagrams using dictionary.
8. Create a menu-driven student management system.
