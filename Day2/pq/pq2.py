class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def increase_salary(self):
        self.salary += self.salary * 0.10
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
        print("-" * 20)

employees = [
    Employee("Adarsh", 60000, "IT"),
    Employee("Aman", 45000, "HR"),
    Employee("Rishav", 80000, "Finance"),
    Employee("Sahil", 52000, "IT"),
    Employee("Rahul", 40000, "Sales")
]

for emp in employees:
    emp.increase_salary()
print("Employee Details:")
for emp in employees:
    emp.display()

high_salary = [emp for emp in employees if emp.salary > 50000]

for emp in high_salary:
    print(emp.name, emp.salary)

avg_salary = sum(emp.salary for emp in employees) / len(employees)
print(avg_salary)