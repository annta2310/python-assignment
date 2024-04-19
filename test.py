# person identity :
# Define a class called Person with two attributes: age and gender
class Person:
    def __init__(self,age,gender):
        self.age = age
        self.gender = gender
# Create an instance of the Person class called user, with an age of 14 and a gender of "female"
user = Person(14,"female")
# Print the value of the gender attribute of the user instance
print (user.gender)  
print (user.age)  


# cat identity:
# Define a class called Cat with three attributes: name, age, and colour
class Cat:
    def __init__(self,name,age,colour):
        self.name = name
        self.age = age
        self.colour = colour
# Create an instance of the Cat class called user, with a name of "mani", an age of 12, and a colour of "brown"
user = Cat("mani",12,"brown")
print(user.name)
print(user.age)
print(user.colour)
