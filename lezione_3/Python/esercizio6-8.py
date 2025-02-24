#esercizio6-8
cane: dict={"animale":"cane", "razza":"labrador", "padrone":"taggiasco"}
gatto: dict={"animale":"gatto", "razza":"siamese", "padrone":"laghetti"}
piccione: dict={"animale":"piccione", "razza":"stefano", "padrone":"benigni"}

pets = [cane, gatto, piccione]

for i in pets:
    print(f"Animale: {i['animale']}")
    print(f"Razza: {i['razza']}")
    print(f"Padrone: {i['padrone']}")
    