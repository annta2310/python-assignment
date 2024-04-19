class Person:
    def __init__(self,name):
        self.name= name


    def greet(self):
        print(f"Hello,{self.name}!")  

    def login():
        valid_username = "user"
        valid_password = "password"


        username = input("Enter your username: ")
        password = input("Enter your password: ")


        if username == valid_username and password == valid_password:
            print("Login successful!")
        else:
            print("Invalid username or password.")
    login()    