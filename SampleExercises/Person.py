class Person:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)

    def details(self):
        print(f"My name is: {self.name}")
        print(f"My Id is: {self.id}")
        

class Student(Person):

    def __init__(self, name, id, major, university_name):
        super().__init__(name, id)
        self.major = major
        self.university_name = university_name

    def details(self):
        super().details()
        print(f"Major: {self.major}")
        print(f"University Name: {self.university_name}")


delphi = Student("Delphi", 26, "Computer Science", "uOttawa")
delphi.details()