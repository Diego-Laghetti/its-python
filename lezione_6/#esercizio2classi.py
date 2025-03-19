#esercizio2classi
class Student:
    def __init__(self, name, studyProgram, age, gender):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"Name: {self.name}, Study Program: {self.studyProgram}, Age: {self.age}, Gender: {self.gender}")

# Create instances
me = Student("Diego", "Computer Science", 19, "Male")
left_neighbour = Student("Claudio", "Medicine", 20, "Male")
right_neighbour = Student("Rachele", "Cybersecurity", 27, "Female")

# Test printInfo method
me.printInfo()
left_neighbour.printInfo()
right_neighbour.printInfo()
