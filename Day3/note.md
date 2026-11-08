1. Functions
Functions are reusable blocks of code.
def calculate_average(numbers):    return sum(numbers) / len(numbers)scores = [80, 90, 70]print(calculate_average(scores))



Important concepts:
- def → defines a function
- Parameters → input values
- return → sends result back
- Local variables → exist inside the function
2. Modules
A module is a Python file containing reusable code or functionality.
import mathprint(math.sqrt(25))



Import specific functions:
from math import sqrtprint(sqrt(36))



Create your own module:

calculator.py
def add(a, b):    return a + b



main.py
import calculatorprint(calculator.add(10, 20))



3. Exception Handling
Exceptions prevent programs from crashing unexpectedly.
try:    num = int(input("Enter number: "))    print(100 / num)except ValueError:    print("Invalid number")except ZeroDivisionError:    print("Cannot divide by zero")finally:    print("Program completed")



Keyword	Purpose
try	Code that may fail
except	Handles the error
else	Runs if no exception occurs
finally	Always executes

4. File Handling
Write a file:
with open("data.txt", "w") as f:    f.write("Hello Python")



Read a file:
with open("data.txt", "r") as f:    content = f.read()print(content)



Modes:
- r → read
- w → write (overwrites)
- a → append
- x → create new file
5. CSV Handling
CSV means Comma-Separated Values.

Example students.csv:
name,age,marks
Rahul,20,85
Aman,21,90
Ravi,19,invalid
Priya,20,95


Python provides the built-in csv module.
import csvwith open("students.csv", "r") as f:    reader = csv.DictReader(f)    for row in reader:        print(row["name"], row["marks"])



DictReader converts each row into a dictionary.



# question below this 
Create a function that returns the maximum number in a list.



Create a module containing multiplication and division functions.



Handle ValueError when converting user input into integers.



Read a CSV and calculate the average marks.



Write a CSV containing only students scoring above 75.



Handle missing age values while reading a CSV.



Count the number of valid and invalid email addresses in a CSV.