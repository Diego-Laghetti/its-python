from users import User, Privileges, Admin

claudia = User("Claudia", "Valore", "Donna", 23, "claudiavalore@gmail.com")

privileges1 = Privileges("ugo")
privileges2 = Privileges(["ugo", "albertone"])

admin1 = Admin(claudia, privileges1)
admin1.user.describe_user()
admin1.privileges.show_privileges()

print("\n------------------\n")

admin2 = Admin(claudia, privileges2)
admin2.user.describe_user()
admin2.privileges.show_privileges()
