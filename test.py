# person identity :
class Person:
    def __init__(self,age,gender):
        self.age = age
        self.gender = gender
user = Person(14,"female")
print (user.gender)  
# cat identity :
class Cat:
    def __init__(self,name,age,colour):
        self.name = name
        self.age = age
        self.colour = colour

user = Cat("mani",12,"brown")
print(user.name)
print(user.age)
print(user.colour)
