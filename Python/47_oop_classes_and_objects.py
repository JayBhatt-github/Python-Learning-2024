class Person :
    name = "john"
    occupation = "product manager"
    age = "27"
    def desc(self):
        print(f"Name:{self.name}\nOccupation:{self.occupation}\nAge:{self.age}\n")
        
        
a = Person()
b = Person()
c = Person()

a.name = "Brayden"
a.occupation = "Administrator"
a.age = "31"

b.name = "Chris"
b.occupation = "Product Designer"
b.age = "26"

b.name = "Anderson"
b.occupation = "Accountant"
b.age = "34"

a.desc()
b.desc()
c.desc()