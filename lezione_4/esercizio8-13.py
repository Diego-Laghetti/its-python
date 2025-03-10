#esercizio8-13
def build_profile(nome, cognome, età, capelli, peso):
    return f"{nome} {cognome}, età {età}, capelli {capelli}, peso {peso}"

profilo = {"nome": "diego", "cognome": "laghetti", "età": 19, "capelli": "marroni", "peso": 80}
profile = build_profile(profilo["nome"], profilo["cognome"], profilo["età"], profilo["capelli"], profilo["peso"])
     
print(profile)


