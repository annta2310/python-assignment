class Person:
    def __init__(self,name):# Constructor method that initializes the name attribut
        self.name= name


    def greet(self):# Method that prints a greeting message
        print(f"Hello,{self.name}!")  

    def login():  # Method that prompts the user to enter their username and password
        valid_username = "user"
        valid_password = "password"


        username = input("Enter your username: ")
        password = input("Enter your password: ")


        if username == valid_username and password == valid_password:
            print("Login successful!!")
        else:
            print("Invalid username or password.")
    login()    