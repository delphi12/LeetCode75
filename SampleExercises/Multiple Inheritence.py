# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Base class 2
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Salary: ${self.salary}")

# Child Class
class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def display_info(self):
        Person.display_info(self)
        Employee.display_info(self)
        print(f"Department: {self.department}")


manager = Manager("Jane Brown", 40, "M789", 75000, "HR")
manager.display_info()
