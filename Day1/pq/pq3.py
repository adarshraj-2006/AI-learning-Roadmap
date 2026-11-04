print("Hello World ! ")

name = input("Enter your name: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


def calculate(a, b):
    return a + b, a - b, a * b

addition, subtraction, multiplication = calculate(num1, num2)

print("\nHello,", name)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)