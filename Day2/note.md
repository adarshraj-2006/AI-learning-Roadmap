
# Python Quick Revision

## 1. Comprehension
Comprehension is a short way to create lists.

```python
nums = [1, 2, 3, 4, 5]
squares = [x*x for x in nums]
even = [x for x in nums if x%2 == 0]
print(squares)
print(even)
```

## 2. Data Processing
Data processing means filtering, sorting and calculating data.

```python
marks = [70, 80, 90, 60]

print(sum(marks))
print(max(marks))
print(min(marks))
print(len(marks))

avg = sum(marks)/len(marks)
print(avg)

passed = [m for m in marks if m >= 70]
print(passed)
```

## 3. OOP in Python
OOP means Object-Oriented Programming.

- Class: Blueprint of objects.
- Object: Instance of class.
- Constructor: `__init__()`
- Self: Refers to current object.
- Inheritance: Reusing parent class.
- Polymorphism: Same method, different behavior.
- Encapsulation: Protecting data.
- Abstraction: Hiding implementation details.

### Example

```python

class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)

s = Student("Raj")
s.display()
```

### Inheritance

```python
class A:
    def show(self):
        print("Parent")

class B(A):
    pass

obj = B()
obj.show()
```
