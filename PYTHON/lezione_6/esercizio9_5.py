#eserczio9_5
class User:
    def __init__(self, first_name, last_name, gender, age, loggingattemtps = 0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.loggingattemtps = loggingattemtps

    def describe_user(self):
        print(f"The name is {self.first_name}")
        print(f"The last name is {self.last_name}")
        print(f"The age is {self.age}")
        print(f"The gender is {self.gender}")
        print(f"The logging attemtps are {self.loggingattemtps}")
        print("------------------")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

    def increment_login_attempts(self, n = 1):
        self.loggingattemtps += n

    def reset_login_attempts(self):
        self.loggingattemtps = 0

claudia = User("Claudia", "Valore", 23, "Donna")

claudia.increment_login_attempts()
claudia.describe_user()
claudia.reset_login_attempts()
claudia.describe_user()
claudia.greet_user()
