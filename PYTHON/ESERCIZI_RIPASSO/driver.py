from persona import Persona 
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

dottore1 = Dottore("Pinco", "Pallino", "Ginecologo", 5000.0)
dottore2 = Dottore("Charlie", "Kirk", "Opinionista", 10.11)

p1 = Paziente("Riccardo", "Paladini", "71")
p2 = Paziente("Emiliano", "De Valeri", "palle")
p3 = Paziente("Diego", "LaghettodellEur", "17")
p4 = Paziente("Luca", "Taggiasco", "16")

pazienti1 = [p1, p2, p3]
pazienti2 = [p4]

dottore1.setAge(31)
dottore2.setAge(1048)

dottore1.doctorGreet()
dottore2.doctorGreet()

fattura1 = Fattura(pazienti1, dottore1)
fattura2 = Fattura(pazienti2, dottore2)


print(f"Salario Dottore 1: {fattura1.getSalary()} euro")
print(f"Salario Dottore 2: {fattura2.getSalary()} euro")

pazienti1.remove(p3)
pazienti2.append(p3)

print(f"Salario Dottore 1: {fattura1.getSalary()} euro")
print(f"Salario Dottore 2: {fattura2.getSalary()} euro")

guadagno_ospedale = fattura1.getSalary()+fattura2.getSalary()
print(f"In totale l'sopedale ha incassato: {guadagno_ospedale} euro!")