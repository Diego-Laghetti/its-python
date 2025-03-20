'''
#persona-testing

#dal file persona.py importa la classe Persona
from persona import Persona

dl:Persona = Persona("Diego", "Laghetti", 19)
print(dl)

print(dl.name, dl.lastname, dl.age)

#sfrutto la funzione displayData della còlasse Persona per visualizzare in output i dati derativi alla persona dl

dl.displayData()
'''

#dal file persona2.py importa la classe Persona
from persona2 import Persona

dl:Persona = Persona()

dl.displayData()

print("-------------------------")

#imposto il nome della persona dl
dl.setName("Diego")
dl.displayData()

#imposto il cognome della persona dl
dl.setLastname("Laghetti")

#imposto l'età della persona dl
dl.setAge(19)

print("-------------------------")

dl.displayData()

print("-------------------------")

print(dl.getName(), dl.getLastname(), dl.getAge())





