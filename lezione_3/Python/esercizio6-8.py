#esercizio6-8
cane: dict={"animale":"cane", "razza":"labrador", "padrone":"taggiasco"}
gatto: dict={"animale":"gatto", "razza":"siamese", "padrone":"laghetti"}
piccione: dict={"animale":"piccione", "razza":"stefano", "padrone":"benigni"}

pets = [cane, gatto, piccione]

for i in pets:
    print(f"animale: {i['animale']}")
    print(f"razza: {i['razza']}")
    print(f"padrone: {i['padrone']}")
    