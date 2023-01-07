class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(self.name, self.age)
        
class Employee(Person):
    def __init__(name, age):
        super().__init__(name, age)
            
a = Employee("Amrit", "20")
a.display()