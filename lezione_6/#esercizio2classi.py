#esercizio2classi

'''1. Write a class called Student with the attributes name (str) and
studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too.'''

#1
class Student:
    def __init__(self,name,studyProgram):
        self.name = name
        self.studyProgram = studyProgram


#3
def printinfo(self):
    print(f"Il nome è {diego.name} ed il corso è {diego.studyProgram}")

#²
diego = Student("Diego", "Python")
alessio = Student("Alessio", "Inglese")
luca = Student("Luca", "Soft Skill")

printinfo()

