class Employee:
    def __init__(self):
        self.name='name'
        self.salary='salary'
        self.deparment='department'
    def incr_sal(self,salary):
        salary=salary*1.10
        print(salary)
    def display(self,name,salary,department):
        print("Name:",name)
        print("Salary:",salary)
        print("Department:",department)

    
