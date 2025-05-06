class Person:
    def __init__(self, name="Aniket", age=26):
        self.name= name
        self.age= age
    def greet(self):
        print(self.name, self.age)
    
p1=Person()
p1.greet()

p2=Person("Bunny", 26)
p2.greet()