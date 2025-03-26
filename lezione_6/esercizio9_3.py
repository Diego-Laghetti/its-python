#esercizio9_3
class User:
    def __init__(self, first_name, last_name, gender, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(f"The name is {self.first_name}")
        print(f"The last name is {self.last_name}")
        print(f"The age is {self.age}")
        print(f"The gender is {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

godwayne = User("Gadwayne", "Rasalan", 24, "Maschio")
luca = User("Luca", "Taggiasco", 45, "Maschio")
claudia = User("Claudia", "Valore", 23, "Donna")

godwayne.describe_user()
luca.describe_user()
claudia.describe_user()

godwayne.greet_user()
luca.greet_user()
claudia.greet_user()

