'''Scrivere, infine, il codice driver che gestisca due dottori e due liste di pazienti. La prima lista di pazienti deve contenere 3 
pazienti, mentre la seconda 1 solo paziente.

    Impostare l'età di ogni medico, affinché i due medici risultino validi!
    Il primo medico e il secondo medico si presentano, richiamando il rispettivo metodo doctorGreet().
    Creare un oggetto fattura chiamato fattura1. Alla fattura 1 devono essere associati il dottore_1 e la lista di 3 pazienti.
    Creare un oggetto fattura chiamato fattura2. Alla fattura 2 devono essere associati il dottore_2 e la lista di un solo paziente.
    Stampare in output il salario di ogni singolo dottore. Ad esempio:

      "Salario Dottore1: ... euro!
       Salario Dottore2: ... euro!"

    Rimuovere un paziente dalla lista dei pazienti del dottore 1 ed inserire tale paziente nella lista del dottore 2.
    Stampare in output il salario di ogni dottore.
    Stampare in output il guadagno totale incassato dall'ospedale. Il guadagno totale viene calcolato sommando i guadagni di ogni dottore.
     Esempio:

"In totale, l'ospedale ha incassato: tot euro!"
'''
from persona import Persona 
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

dottore1 = Dottore("Pinco", "Pallino", "Ginecologo", 5000)
dottore2 = Dottore("Charlie", "Kirk", "Opinionista", 10)

p1 = Paziente("Riccardo", "Paladini", "71")
p2 = Paziente("Emiliano", "De Valeri", "palle")
p3 = Paziente("Diego", "LaghettodellEur", "17")
p4 = Paziente("Luca", "Taggiasco", "16")

pazienti1 = [p1, p2, p3]
pazienti2 = [p4]

dottore1.SetEta(40)
dottore2.SetEta(35)

dottore1.doctorGreet()
dottore2.doctorGreet()

fattura1 = Fattura(pazienti1, dottore1)
fattura2 = Fattura(pazienti2, dottore2)

print(f"Salario {dottore1.GetCognome()}: {fattura1.getSalary()} euro!")
print(f"Salario {dottore2.GetCognome()}: {fattura2.getSalary()} euro!")

paziente_da_spostare = p1  
fattura1.removePatient(paziente_da_spostare.GetIdCode())
fattura2.addPatient(paziente_da_spostare)

print(f"Dopo lo spostamento del paziente...")
print(f"Salario {dottore1.GetCognome()}: {fattura1.getSalary()} euro!")
print(f"Salario {dottore2.GetCognome()}: {fattura2.getSalary()} euro!")

guadagno_totale = fattura1.getSalary() + fattura2.getSalary()
print(f"In totale, l'ospedale ha incassato: {guadagno_totale} euro!")


