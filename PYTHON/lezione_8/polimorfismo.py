from persona import Persona
from alieno import Alieno

#creare un oggetto p della classe Persona
p: Persona = Persona("Diego", "Laghetti", 19)

#visualizzare le informazioni dell'oggetto p
print(p)

#creare un oggetto et della classe Alieno
et: Alieno = Alieno("Ciccio")

#visualizzare le informazioni dell'oggetto et
print(et)

#fare in modo che l'oggetto p invochi il metodo speak()
p.speak()

#fare in modo che l'oggetto et invochi il metodo speak()
et.speak()
