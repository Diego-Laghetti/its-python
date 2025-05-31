class User:
    def __init__(self, first_name, last_name, gender, age, email, loggingattemtps=0):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.email = email
        self.loggingattemtps = loggingattemtps

    def describe_user(self):
        print(f"The name is {self.first_name}")
        print(f"The last name is {self.last_name}")
        print(f"The age is {self.age}")
        print(f"The gender is {self.gender}")
        print(f"The logging attemtps are {self.loggingattemtps}")
        print(f"The email is {self.email}")
        print("------------------")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

    def increment_login_attempts(self, n=1):
        self.loggingattemtps += n

    def reset_login_attempts(self):
        self.loggingattemtps = 0


class Privileges:
    def __init__(self, privilege=None):
        self.p = []
        if privilege:
            if isinstance(privilege, list):
                self.set_privilege(privilege)
            else:
                self.add_privilege(privilege)

    def add_privilege(self, privilege):
        self.p.append(privilege)

    def set_privilege(self, privilege: list):
        self.p = privilege

    def show_privileges(self):
        print("Privileges:")
        if self.p:
            for priv in self.p:
                print(f"- {priv}")
        else:
            print("No privileges assigned.")


class Admin:
    def __init__(self, user: User, privileges: Privileges):
        self.user = user
        self.privileges = privileges

