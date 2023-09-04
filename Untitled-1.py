class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.id} {self.name} {self.age} {self.salary}"

employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

def sort_employees(employees, key):
    if key == "age":
        employees.sort(key=lambda x: x.age)
    elif key == "name":
        employees.sort(key=lambda x: x.name)
    elif key == "salary":
        employees.sort(key=lambda x: x.salary)

def print_employees(employees):
    for employee in employees:
        print(employee)

key = input("Enter sorting parameter (age/name/salary): ")
sort_employees(employees, key)
print_employees(employees)
