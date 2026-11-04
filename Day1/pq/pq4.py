
empl = {
    101: {"name": "Adarsh", "salary": 30000, "department": "IT"},
    102: {"name": "Ravi", "salary": 25000, "department": "HR"},
    103: {"name": "Neha", "salary": 40000, "department": "IT"},
    104: {"name": "Aman", "salary": 35000, "department": "Finance"}
}

for id, data in empl.items():
    print(data["name"], data["salary"])

it = {
    id: data for id, data in empl.items()
    if data["department"] == "IT"
}
print("IT employees:", it)

topper = max(empl.items(), key=lambda x: x[1]["salary"])
print("Highest salary:", topper)

for data in empl.values():
    data["salary"] *= 1.10


id = int(input("Enter ID: "))
name = input("Enter name: ")
salary = int(input("Enter salary: "))
department = input("Enter department: ")

empl[id] = {
    "name": name,
    "salary": salary,
    "department": department
}

delete_id = int(input("Enter ID to delete: "))
empl.pop(delete_id, None)

avg = sum(d["salary"] for d in empl.values()) / len(empl    )
print("Average salary:", avg)


high_salary = {
    id: d for id, d in empl.items()
    if d["salary"] > 30000
}
print("High salary employees:", high_salary)


print("Final dictionary:", employees)
