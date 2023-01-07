#Polymorphism

def sum(x,y,z=0,p=0):
    return x + y + z + p
print(sum(2,3))
print(sum(2,3,4,5))




class India():
  def capital(self):
    print("New Delhi is the captial of India")
  def language(self):
    print("Multiple language are spoken in India")

class USA():
  def capital(self):
    print("washington DC")

  def language(self):
    print("English")

obj1 = India()
obj2 = USA()

obj1 .capital()
obj1 .language()

obj2 .capital()
obj2 .language()




class Bird():
  def intro(self):
    print("This is a bird class")

  def flight(self):
    print("Birds")

class Parrot(Bird):
  def flight(self):
    print("Parrot can fly")

class Ostrich(Bird):
  def flight(self):
    print("Ostrich cannot fly")

obj1 = Bird()
obj2 = Parrot()
obj3 = Ostrich()

obj1.intro()
obj1.flight()

obj2.intro()
obj2.flight()

obj3.intro()
obj3.flight()
